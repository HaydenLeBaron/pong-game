# Pong game
#
# Based off of code from https://www.youtube.com/watch?v=Qf3-aDXG8q4


import pygame, sys, random


# Constants
# -----------------------------------
BALL_LENGTH = 30
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 140
BG_COLOR = pygame.Color('grey40')
LIGHT_GREY = (10, 10, 10)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
FRAME_RATE = 60




class Ball:

    def __init__(self, diameter=30, color_tuple=(30, 30, 0), x_speed=7, y_speed=7):

        global SCREEN_WIDTH, SCREEN_HEIGHT

        self.diameter = diameter
        self.color_tuple = color_tuple
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - self.diameter/2,
                                SCREEN_HEIGHT/2 - self.diameter/2,
                                BALL_LENGTH, BALL_LENGTH)
        self.x_speed = x_speed
        self.y_speed = y_speed


    def move_to_next_frame(self):

        global SCREEN_WIDTH, SCREEN_HEIGHT

        # Move ball
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Bounce balls on wall collision
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
           self.y_speed *= -1

        # Restart ball if it hits the goal
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.restart()

        # Bounce balls on paddle collision
        if self.rect.colliderect(player) or self.rect.colliderect(opponent):
            self.x_speed *= -1

    def restart(self):
        ball.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # Move ball to center
        self.x_speed *= random.choice((1, -1))
        self.y_speed *= random.choice((1, -1))



class Paddle:
    pass

class PlayerPaddle:
    pass

class AiPaddle:
    pass


# Drawing helpers
# -----------------------------------


def player_animation():

    player.y += player_speed  # Move player

    # Don't let player move off screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def opponent_ai():

    # Move opponent
    if opponent.top < ball.rect.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.rect.y:
        opponent.bottom -= opponent_speed

    # Don't let opponent move off screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT



# General setup
# -----------------------------------

pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
# -----------------------------------


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')


# Game Rectangles
# -----------------------------------

# NOTE: origin (0, 0) is in top left corner

ball = Ball(30, pygame.Color('yellow'),
            7 * random.choice((1, -1)),
            7 * random.choice((1, -1)))

player = pygame.Rect(SCREEN_WIDTH - 20,
                   SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2,
                     PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10,
                   SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2,
                     PADDLE_WIDTH, PADDLE_HEIGHT)

player_speed = 0
opponent_speed = 7



# Game loop
# -----------------------------------

while True:
    # Handle player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


    # Shift game object locations
    ball.move_to_next_frame()
    player_animation()
    opponent_ai()

    # Draw game objects
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LIGHT_GREY, player)
    pygame.draw.rect(screen, LIGHT_GREY, opponent)
    pygame.draw.aaline(screen, LIGHT_GREY,
                       (SCREEN_WIDTH/2, 0),
                       (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, ball.color_tuple, ball.rect)

    # Updating the window
    pygame.display.flip()
    clock.tick(FRAME_RATE)
