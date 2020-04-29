# Pong game
#
# Based off of code from https://www.youtube.com/watch?v=Qf3-aDXG8q4


import pygame, sys, random


# Constants
# -----------------------------------
BALL_LENGTH = 30
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 140
BG_COLOR = pygame.Color('grey12')
LIGHT_GREY = (10, 10, 10)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960




class Ball:
    def __init__(self, diameter=30, color=pygame.Color('yellow')):
        self.diameter = diameter
        self.color = color
        #self.rect = TODO
       

class Paddle:
    pass

class PlayerPaddle:
    pass

class AiPaddle:
    pass

# Drawing helpers
# -----------------------------------

def ball_animation():

    global ball_speed_x, ball_speed_y  # TODO: refactor to avoid globals

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce balls on wall collision
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Restart ball if it hits the goal
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_restart()

    # Bounce balls on paddle collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():

    player.y += player_speed  # Move player

    # Don't let player move off screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def opponent_ai():

    # Move opponent
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Don't let opponent move off screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))



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

ball = pygame.Rect(SCREEN_WIDTH/2 - BALL_LENGTH/2,
                   SCREEN_HEIGHT/2 - BALL_LENGTH/2,
                   BALL_LENGTH, BALL_LENGTH)
player = pygame.Rect(SCREEN_WIDTH - 20,
                   SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2,
                     PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10,
                   SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2,
                     PADDLE_WIDTH, PADDLE_HEIGHT)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))


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
    ball_animation()
    player_animation()
    opponent_ai()

    # Draw game objects
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LIGHT_GREY, player)
    pygame.draw.rect(screen, LIGHT_GREY, opponent)
    pygame.draw.ellipse(screen, LIGHT_GREY, ball)
    pygame.draw.aaline(screen, LIGHT_GREY,
                       (SCREEN_WIDTH/2, 0),
                       (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
