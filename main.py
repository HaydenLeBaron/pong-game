#
# main.py

"""This file contains the starting point for this pong game,
as well as some helper methods."""

import pygame, sys, random
import globals
import events
from paddle import _Paddle
from playerpaddle import PlayerPaddle
from aipaddle import AIPaddle
from ball import Ball


def main():
    """The starting point for this program."""

    # General setup
    # -----------------------------------

    globals.init()
    events.init()
    pygame.init()
    game_on = True
    clock = pygame.time.Clock()
    pygame.display.set_caption('Pong')

    score_font = pygame.font.SysFont('Helvetica',  # Init text drawer
                                   48, bold=True, italic=False)
    victory_font = pygame.font.SysFont('Helvetica',  # Init text drawer
                                       100, bold=True, italic=True)


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
    player_score_surface = score_font.render(str(player_score),
                                           True, globals.player.color_tuple)
    bot_score_surface = score_font.render(str(bot_score),
                                        True, globals.bot.color_tuple)
    victory_message_surface = None


    # Game loop
    # -----------------------------------

    while game_on:

        for event in pygame.event.get():

            #=================================
            # DEBUG OUTPUT
            #print('event: ', event)
            #print('type: ', event.type)
            #=================================

            if player_score >= globals.POINTS_TO_WIN:
                pygame.event.post(events.right_side_wins)
            elif bot_score >= globals.POINTS_TO_WIN:
                pygame.event.post(events.left_side_wins)

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
            if event.type == events.LEFT_GOAL_SCORED_IN_TYPE or \
                    event.type == events.RIGHT_GOAL_SCORED_IN_TYPE:
                globals.player.reset_position('right')
                globals.bot.reset_position('left')
                globals.ball.restart()
                pygame.time.delay(1000)  # Pause game for 1000 ms

            if event.type == events.LEFT_GOAL_SCORED_IN_TYPE:
                print('LEFT GOAL SCORED IN')
                player_score += 1
            if event.type == events.RIGHT_GOAL_SCORED_IN_TYPE:
                print('RIGHT GOAL SCORED IN')
                bot_score += 1
            if event.type == events.LEFT_SIDE_WINS_TYPE:
                print('LEFT SIDE WINS')
                victory_message_surface = victory_font.render('LEFT SIDE WINS!',
                                                       True,
                                                       globals.bot.color_tuple)
            if event.type == events.RIGHT_SIDE_WINS_TYPE:
                print('RIGHT SIDE WINS')
                victory_message_surface = victory_font.render('RIGHT SIDE WINS!',
                                                       True,
                                                       globals.player.color_tuple)

        # Shift game object locations
        globals.ball.move_to_next_frame()
        globals.player.move_to_next_frame()
        globals.bot.move_to_next_frame()

        # Draw game objects
        globals.screen.fill(globals.BG_COLOR)
        pygame.draw.rect(globals.screen,
                         globals.player.color_tuple,
                         globals.player)
        pygame.draw.rect(globals.screen,
                         globals.bot.color_tuple,
                         globals.bot)
        pygame.draw.aaline(globals.screen,
                           globals.MIDLINE_COLOR_TUPLE,
                        (globals.SCREEN_WIDTH/2, 0),
                        (globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT))
        pygame.draw.ellipse(globals.screen,
                            globals.ball.color_tuple,
                            globals.ball.rect)

        # Draw score
        player_score_surface = score_font.render(str(player_score),
                                           True, globals.player.color_tuple)
        bot_score_surface = score_font.render(str(bot_score),
                                        True, globals.bot.color_tuple)
        globals.screen.blit(player_score_surface, (globals.SCREEN_WIDTH -80, 20))
        globals.screen.blit(bot_score_surface, (60, 20))

        if victory_message_surface is not None:
            globals.screen.blit(victory_message_surface,
                                (globals.SCREEN_WIDTH/2 - 400,
                                 globals.SCREEN_HEIGHT/2))
            game_on = False  # The game loop will not run again

        # Update the window
        pygame.display.flip()
        clock.tick(globals.FRAME_RATE)


    pygame.time.delay(3000)
    pygame.quit()


if __name__ == '__main__':
    main()
