# Pong game
#
# Originally based off of code from https://www.youtube.com/watch?v=Qf3-aDXG8q4


# TODO: doc everything
#
# IDEAS
# * Score
# * PVP (wasd vs arrows)
# * 2 player co-op

import pygame, sys, random


# Constants
# -----------------------------------

BG_COLOR = pygame.Color('black')
MIDLINE_COLOR_TUPLE = (255, 255, 255)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
FRAME_RATE = 60


class Ball:

    def __init__(self, diameter=30, color_tuple=(30, 30, 0), x_speed=7, y_speed=7):

        global SCREEN_WIDTH, SCREEN_HEIGHT

        self.diameter = diameter
        self.color_tuple = color_tuple
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - diameter/2,
                                SCREEN_HEIGHT/2 - diameter/2,
                                diameter, diameter)
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
        if self.rect.colliderect(player) or self.rect.colliderect(bot):
            self.x_speed *= -1

    def restart(self):
        ball.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # Move ball to center
        self.x_speed *= random.choice((1, -1))
        self.y_speed *= random.choice((1, -1))



class Paddle:
    def __init__(self, color_tuple, side):
        # side -- a string (either 'right' or 'left'), indicating what side the paddle is on (default: right)
        
        global SCREEN_HEIGHT, SCREEN_WIDTH

        self.width = 20
        self.height = 150
        self.color_tuple = color_tuple
        self.y_speed = 0

        if side == 'right':
            self.rect = pygame.Rect(SCREEN_WIDTH - 20,
                                    SCREEN_HEIGHT/2 - self.height/2,
                                    self.width, self.height)
        else:
            self.rect = pygame.Rect(10,
                                    SCREEN_HEIGHT/2 - self.height/2,
                                    self.width, self.height)



class PlayerPaddle(Paddle):

    def __init__(self, color_tuple, side):
        super().__init__(color_tuple, side)

    def move_to_next_frame(self):

        global SCREEN_HEIGHT
        player.rect.y += player.y_speed  # Move player

        # Don't let player move off screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class AIPaddle(Paddle):

    def __init__(self, color_tuple, side, target_ball):
        super().__init__(color_tuple, side)
        self.y_speed = 7
        self.target_ball = target_ball

    def move_to_next_frame(self):

        global SCREEN_HEIGHT
       
        # Move bot
        if self.rect.top < self.target_ball.rect.y:
            self.rect.top += self.y_speed
        if self.rect.bottom > self.target_ball.rect.y:
            self.rect.bottom -= self.y_speed

        # Don't let bot move off screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT



# Drawing helpers
# -----------------------------------





# General setup
# -----------------------------------

pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
# -----------------------------------


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')


# Game Objects
# -----------------------------------

# NOTE: origin (0, 0) is in top left corner

ball = Ball(30, pygame.Color('yellow'),
            7 * random.choice((1, -1)),
            7 * random.choice((1, -1)))

player = PlayerPaddle((0, 0, 240), 'right')
bot = AIPaddle((240, 0, 0), 'left', ball)



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
                player.y_speed += 7
            if event.key == pygame.K_UP:
                player.y_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.y_speed -= 7
            if event.key == pygame.K_UP:
                player.y_speed += 7


    # Shift game object locations
    ball.move_to_next_frame()
    player.move_to_next_frame()
    bot.move_to_next_frame()

    # Draw game objects
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, player.color_tuple, player)
    pygame.draw.rect(screen, bot.color_tuple, bot)
    pygame.draw.aaline(screen, MIDLINE_COLOR_TUPLE,
                       (SCREEN_WIDTH/2, 0),
                       (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, ball.color_tuple, ball.rect)

    # Updating the window
    pygame.display.flip()
    clock.tick(FRAME_RATE)
