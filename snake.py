import time

import pygame
from pygame.locals import *
from enum import Enum

# Declare Direction class.
class Direction(Enum):
    Stagnant = 0
    Up = 1
    Down = 2
    Left = 3
    Right = 4

# initialize the window.
pygame.init()

# Set the screen dimensions and display.
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake")

# Create the snake.
cell_size = 10
snake_speed = 10
direction = Direction.Stagnant
snake = [[int(screen_width/2), int(screen_height/2)]]
snake.append([int(screen_width/2), int(screen_height/2 + 10)])
snake.append([int(screen_width/2), int(screen_height/2 + 20)])

# Declare game colors.
background_color = (255, 200, 150)
head_color = (255, 0, 0)
body_outer_color = (50, 255, 50)
body_inner_color = (50, 50, 255)


def draw_screen():
    screen.fill(background_color)

def draw_snake_segment(x, y, outer_color, inner_color):
    """
    This function draws a snake segment of the desired color to the given coordinates on the screen.
    :param x: The x-coordinate of the snake segment.
    :param y: The y-coordinate of the snake segment.
    :param outer_color: The outer color of the snake segment.
    :param inner_color: The inner color of the snake segment.
    :return: void.
    """
    pygame.draw.rect(screen, outer_color, (x, y, cell_size, cell_size))
    pygame.draw.rect(screen, inner_color, (x + 1, y + 1, cell_size - 2, cell_size - 2))

run = True
while run:

    # Draw screen.
    draw_screen()

    # Check events.
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != Direction.Down:
                direction = Direction.Up
            elif event.key == K_DOWN and direction != Direction.Up:
                direction = Direction.Down
            elif event.key == K_RIGHT and direction != Direction.Left:
                direction = Direction.Right
            elif event.key == K_LEFT and direction != Direction.Right:
                direction = Direction.Left

    # Update the snake list to reflect the snake's movement.
    if direction != Direction.Stagnant:
        snake = snake[-1:] + snake[:-1] # last elm moved to front.
        prevX = snake[1][0]
        prevY = snake[1][1]
        if direction == Direction.Up:
            snake[0] = [prevX, prevY - snake_speed]
        elif direction == Direction.Down:
            snake[0] = [prevX, prevY + snake_speed]
        elif direction == Direction.Left:
            snake[0] = [prevX - snake_speed, prevY]
        elif direction == Direction.Right:
            snake[0] = [prevX + snake_speed, prevY]

    # Draw the snake.
    isHead = True
    for segment in snake:
        if isHead:
            draw_snake_segment(segment[0], segment[1], head_color, head_color)
            isHead = False
        else:
            draw_snake_segment(segment[0], segment[1], body_outer_color, body_inner_color)

    # Update display.
    pygame.display.update()

    time.sleep(0.04)

pygame.quit()