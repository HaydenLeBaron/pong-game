#
# main.py
#

import pygame, sys, random

import globals
from paddle import _Paddle
from playerpaddle import PlayerPaddle
from aipaddle import AIPaddle
from ball import Ball


def main():

    globals.init()

    # General setup
    # -----------------------------------

    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    # -----------------------------------


    pygame.display.set_caption('Pong')


    # Game Objects
    # -----------------------------------

    # NOTE: Origin (0,0) is in top left corner of screen
    #
    globals.ball = Ball(30, pygame.Color('yellow'),
                7 * random.choice((1, -1)),
                7 * random.choice((1, -1)))
    globals.player = PlayerPaddle((0, 0, 240), 'right')
    globals.bot = AIPaddle((240, 0, 0), 'left', globals.ball)



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
                    globals.player.y_speed += 7
                if event.key == pygame.K_UP:
                    globals.player.y_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    globals.player.y_speed -= 7
                if event.key == pygame.K_UP:
                    globals.player.y_speed += 7


        # Shift game object locations
        globals.ball.move_to_next_frame()
        globals.player.move_to_next_frame()
        globals.bot.move_to_next_frame()

        # Draw game objects
        globals.screen.fill(globals.BG_COLOR)
        pygame.draw.rect(globals.screen, globals.player.color_tuple, globals.player)
        pygame.draw.rect(globals.screen, globals.bot.color_tuple, globals.bot)
        pygame.draw.aaline(globals.screen, globals.MIDLINE_COLOR_TUPLE,
                        (globals.SCREEN_WIDTH/2, 0),
                        (globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT))
        pygame.draw.ellipse(globals.screen, globals.ball.color_tuple, globals.ball.rect)

        # Updating the window
        pygame.display.flip()
        clock.tick(globals.FRAME_RATE)


if __name__ == '__main__':
    main()
