import pygame
import button
from pygame import QUIT

# set the size of the window
score1, score2 = 0, 0
width = 800
height = 500
ball_radius = 15
rectangle_width, rectangle_length = 20, 100
black = (0, 0, 0)
gameWindow = pygame.display.set_mode((width, height))
back_ground = pygame.image.load("../Images/background.jpg")
running = True

restart_image = pygame.image.load('../Images/restart.png').convert_alpha()
restart_button = button.Button(325, 200, restart_image, 11)


def create_Window(w, h, background):
    # initialize the pygame
    pygame.init()
    # title of the window
    pygame.display.set_caption("Ball Game")
    # backgroundImage for window
    background_image = pygame.transform.scale(background, (w, h))
    pygame.display.flip()
    return background_image


def obstacles():
    # Ball
    ball = pygame.Rect(width / 2, height / 2, 15, ball_radius)
    # speed of ball
    x_speedBall, y_speedBall = 1, 1
    score1, score2 = 0, 0

    # Rectangles
    player1 = pygame.Rect(0, height / 2 - 40, rectangle_width, rectangle_length)
    player2 = pygame.Rect(width - 20, height / 2 - 40, rectangle_width, rectangle_length)
    return ball, player1, player2, x_speedBall, y_speedBall, score1, score2


def rectangle_Movement(key_Pressed, rect1, rect2):
    if key_Pressed[pygame.K_w]:
        if rect1.top > 0:
            rect1.top -= 1

    if key_Pressed[pygame.K_s]:
        if rect1.bottom < height:
            rect1.bottom += 1

    if key_Pressed[pygame.K_UP]:
        if rect2.top > 0:
            rect2.top -= 1

    if key_Pressed[pygame.K_DOWN]:
        if rect2.bottom < height:
            rect2.bottom += 1


def move_Ball(ball, x_, y_, s1, s2, rect1, rect2):
    gameover = False
    # sound of the ball
    ball_sound = pygame.mixer.Sound("../Sounds/ball_sound.mp3")
    # ball reaches the bottom of the window
    if ball.y >= height - ball_radius:
        y_ = -1
        ball_sound.play()
    # ball reaches the top of the window
    elif ball.y - ball_radius <= 0:
        y_ = 1
        ball_sound.play()
    # ball reaches the left side of the window
    elif ball.x <= 0:
        gameover = True
        x_, y_ = 0, 0
    # ball reaches the right side of the window
    elif ball.x + ball_radius >= width:
        gameover = True
        x_, y_ = 0, 0
        # if ball meets the rectangle1
    elif ball.x <= rectangle_width and ball.y + ball_radius >= rect1.y and ball.y - ball_radius <= rect1.y + rectangle_length:
        s1 += 1
        x_ *= -2
        y_ += 2
        ball_sound.play()
    # if ball meets the rectangle2
    elif ball.x + ball_radius >= width - rectangle_width and ball.y + ball_radius >= rect1.y and ball.y - ball_radius <= rect2.y + rectangle_length:
        s2 += 1
        x_ *= -2
        y_ += 2
        ball_sound.play()
    return x_, y_, s1, s2, gameover


def restart_Pong_Game(s1, s2, run, ball, rect1, rect2, xs, ys):
    run = True
    ball, rect1, rect2, xs, ys, s1, s2 = obstacles()
    return run, ball, rect1, rect2, score1, score2, xs, ys


def game_over(score1, score2):
    if score1 < score2:
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 30)
        winner = font.render('Player ' + str(2) + ' is the winner!', True, black)
    elif score2 < score1:
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 30)
        winner = font.render('Player ' + str(1) + ' is the winner!', True, black)
    elif score1 == score2:
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 30)
        winner = font.render('No winner!', True, black)
    return winner

#  main function
def main(running):
    background = create_Window(width, height, back_ground)
    winner = ''
    ball, rectangle1, rectangle2, x_speed, y_speed, score1, score2 = obstacles()

    # helps to keep showing the background on screen
    while running:
        # gets the key
        keyPressed = pygame.key.get_pressed()
        rectangle_Movement(keyPressed, rectangle1, rectangle2)
        x_speed, y_speed, score1, score2, isgameover = move_Ball(ball, x_speed, y_speed, score1, score2, rectangle1, rectangle2)

        ball.x += x_speed
        ball.y += y_speed

        # filling the background so that the objects move properly
        gameWindow.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 15)
        score1_text = font.render('SCORE: ' + str(score1), True, black)
        score2_text = font.render('SCORE: ' + str(score2), True, black)

        if isgameover:
            winner = game_over(score1, score2)
            gameWindow.blit(winner, (310, 160))
            restart_button.draw(gameWindow)
        gameWindow.blit(score1_text, (20, 20))
        gameWindow.blit(score2_text, (width - 70, 20))
        pygame.draw.rect(gameWindow, "hotpink", rectangle1)
        pygame.draw.rect(gameWindow, "cyan", rectangle2)
        pygame.draw.circle(gameWindow, "lime", ball.center, 10)

        pygame.display.update()

    pygame.quit()
