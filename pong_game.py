import random

import pygame
from pygame import QUIT

# set the size of the window
width = 800
height = 500
gameWindow = pygame.display.set_mode((width, height))
back_ground = pygame.image.load('Images/paint-stains-blend-gradient.jpg')


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
    ball = pygame.Rect(width / 2, height / 2, 15, 15)
    # speed of ball
    x_speedBall, y_speedBall = 1, 1

    # Rectangles
    player1 = pygame.Rect(0, height / 2 - 40, 20, 100)
    player2 = pygame.Rect(width - 20, height / 2 - 40, 20, 100)
    return ball, player1, player2, x_speedBall, y_speedBall


def rectangle_Movement(key_Pressed, rect1, rect2):
    if keyPressed[pygame.K_w]:
        if rect1.top > 0:
            rect1.top -= 2

    if keyPressed[pygame.K_s]:
        if rect1.bottom < height:
            rect1.bottom += 2

    if keyPressed[pygame.K_UP]:
        if rect2.top > 0:
            rect2.top -= 2

    if keyPressed[pygame.K_DOWN]:
        if rect2.bottom < height:
            rect2.bottom += 2


def move_Ball(ball, x, y):
    if ball.y >= height:
        y = -1
    if ball.y <= 0:
        y = 1
    if ball.x <= 0:
        x, y = random.choice([1, -1]), random.choice([1, -1])
    if ball.x >= width:
        x, y = random.choice([1, -1]), random.choice([1, -1])
    return x, y

#  main function
if __name__ == "__main__":
    back_ground = create_Window(width, height, back_ground)

    ball, rectangle1, rectangle2, x_speed, y_speed = obstacles()

    # set the window to be able to close it
    running = True
    # helps to keep showing the background on screen
    while running:
        # gets the key
        keyPressed = pygame.key.get_pressed()
        rectangle_Movement(keyPressed, rectangle1, rectangle2)
        x_speed, y_speed = move_Ball(ball, x_speed, y_speed)

        ball.x += x_speed * 2
        ball.y += y_speed * 2

        # filling the background so that the objects move properly
        gameWindow.blit(back_ground, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        pygame.draw.rect(gameWindow, "hotpink", rectangle1)
        pygame.draw.rect(gameWindow, "cyan", rectangle2)
        pygame.draw.circle(gameWindow, "lime", ball.center, 10)

        pygame.display.update()

    pygame.quit()
