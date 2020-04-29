#
# main.py
#

import pygame, sys, random
import globals
import events
from paddle import _Paddle
from playerpaddle import PlayerPaddle
from aipaddle import AIPaddle
from ball import Ball


def main():


    # General setup
    # -----------------------------------

    globals.init()
    events.init()
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Pong')

    gamefont = pygame.font.SysFont('Helvetica',  # Init text drawer
                                   48, bold=True, italic=False)

    # Game Objects
    # -----------------------------------

    globals.ball = Ball(30, pygame.Color('yellow'),
                7 * random.choice((1, -1)),
                7 * random.choice((1, -1)))
    globals.player = PlayerPaddle((0, 0, 240), 'right')
    globals.bot = AIPaddle((240, 0, 0), 'left', globals.ball)


    # Init score
    # -----------------------------------

    player_score = 0
    bot_score = 0
    player_score_surface = gamefont.render(str(player_score),
                                           True, globals.player.color_tuple)
    bot_score_surface = gamefont.render(str(bot_score),
                                        True, globals.bot.color_tuple)


    # Game loop
    # -----------------------------------



    while True:

        for event in pygame.event.get():
            print('event: ', event)
            print('type: ', event.type)
            # Handle player input events
            if event.type == pygame.QUIT:  # Exit the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Keydown controls
                if event.key == pygame.K_DOWN:
                    globals.player.y_speed += 7
                if event.key == pygame.K_UP:
                    globals.player.y_speed -= 7
            if event.type == pygame.KEYUP:    # Keyup controls
                if event.key == pygame.K_DOWN:
                    globals.player.y_speed -= 7
                if event.key == pygame.K_UP:
                    globals.player.y_speed += 7

            #===========================================
            # NOTE: TEST EVENT EXAMPLE
            # Handle test events
            #if event.type == events.TEST_EVENT_TYPE:
            #    print('TEST_EVENT_PROCESSED')
            #===========================================


            # Handle goal score events
            if event.type == events.LEFT_GOAL_SCORED_IN_TYPE:
                print('LEFT GOAL SCORED IN')
                player_score += 1
            if event.type == events.RIGHT_GOAL_SCORED_IN_TYPE:
                print('RIGHT GOAL SCORED IN')
                bot_score += 1

           

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


        # Draw score
        globals.screen.blit(player_score_surface, (globals.SCREEN_WIDTH -80, 20))
        globals.screen.blit(bot_score_surface, (60, 20))

        # Updating the window
        pygame.display.flip()
        clock.tick(globals.FRAME_RATE)


if __name__ == '__main__':
    main()
