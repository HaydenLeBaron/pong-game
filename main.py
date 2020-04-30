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

    # ==========================================================
    # General setup
    # ==========================================================

    globals.init()
    events.init()
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Pong')

    score_font = pygame.font.SysFont('Helvetica',  # Init text drawer
                                   48, bold=True, italic=False)
    victory_font = pygame.font.SysFont('Helvetica',  # Init text drawer
                                       100, bold=True, italic=True)

    # ==========================================================
    # Init game objects
    # ==========================================================

    globals.ball = Ball(30, pygame.Color('yellow'),
                globals.DEF_BALL_SPEED * random.choice((1, -1)),
                globals.DEF_BALL_SPEED * random.choice((1, -1)))
    globals.player1 = PlayerPaddle(globals.P1_COLOR_TUPLE, 'right')

    if globals.game_mode == 'pvp':
        globals.player2 = PlayerPaddle(globals.P2_COLOR_TUPLE, 'left')
    else:  # if globals.game_mode == 'single_player'
        globals.player2 = AIPaddle(globals.P2_COLOR_TUPLE, 'left', globals.ball)

   
    # ==========================================================
    # Init game flags
    # ==========================================================

    game_on = True
    was_point_scored = False


    # ==========================================================
    # Init score
    # ==========================================================

    player1_score = 0
    player2_score = 0
    player1_score_surface = score_font.render(str(player1_score),
                                           True, globals.player1.color_tuple)
    player2_score_surface = score_font.render(str(player2_score),
                                        True, globals.player2.color_tuple)
    victory_message_surface = None


    # ==========================================================
    # Game loop
    # ==========================================================

    while game_on:

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Event processing loop
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        for event in pygame.event.get():

            ##################################
            # DEBUG OUTPUT
            #print('event: ', event)
            #print('type: ', event.type)
            ##################################

            # Handle victory events
            # ---------------------------------------------
            if player1_score >= globals.POINTS_TO_WIN:
                pygame.event.post(events.right_side_wins)
            elif player2_score >= globals.POINTS_TO_WIN:
                pygame.event.post(events.left_side_wins)


            # Handle quit event
            # ---------------------------------------------
            if event.type == pygame.QUIT:  # Exit the game
                pygame.quit()
                sys.exit()


            # Handle player1 input events
            # ---------------------------------------------
            if event.type == pygame.KEYDOWN:  # Keydown controls
                if event.key == pygame.K_DOWN:
                    globals.player1.y_speed += globals.DEF_PADDLE_SPEED
                if event.key == pygame.K_UP:
                    globals.player1.y_speed -= globals.DEF_PADDLE_SPEED
            if event.type == pygame.KEYUP:    # Keyup controls
                if event.key == pygame.K_DOWN:
                    globals.player1.y_speed -= globals.DEF_PADDLE_SPEED
                if event.key == pygame.K_UP:
                    globals.player1.y_speed += globals.DEF_PADDLE_SPEED


            # Handle player2 input events (if in a multiplayer mode)
            # ---------------------------------------------

            if globals.game_mode == 'pvp':
                if event.type == pygame.KEYDOWN:  # Keydown controls
                    if event.key == pygame.K_s:
                        globals.player2.y_speed += globals.DEF_PADDLE_SPEED
                    if event.key == pygame.K_w:
                        globals.player2.y_speed -= globals.DEF_PADDLE_SPEED
                if event.type == pygame.KEYUP:    # Keyup controls
                    if event.key == pygame.K_s:
                        globals.player2.y_speed -= globals.DEF_PADDLE_SPEED
                    if event.key == pygame.K_w:
                        globals.player2.y_speed += globals.DEF_PADDLE_SPEED

            # Handle goal score events
            # ---------------------------------------------

            if event.type == events.LEFT_GOAL_SCORED_IN_TYPE or \
                    event.type == events.RIGHT_GOAL_SCORED_IN_TYPE:
                globals.player1.reset_position('right')
                globals.player2.reset_position('left')
                globals.ball.restart()
                was_point_scored = True
                if event.type == events.LEFT_GOAL_SCORED_IN_TYPE:
                    print('LEFT GOAL SCORED IN')
                    player1_score += 1
                    victory_message_surface = victory_font.render('right\'s point!',
                                                                True,
                                                                globals.player1.color_tuple)
                elif event.type == events.RIGHT_GOAL_SCORED_IN_TYPE:
                    print('RIGHT GOAL SCORED IN')
                    player2_score += 1
                    victory_message_surface = victory_font.render('left\'s point!',
                                                                True,
                                                                globals.player2.color_tuple)
            else:
                victory_message_surface = None


            if event.type == events.LEFT_SIDE_WINS_TYPE:
                print('LEFT SIDE WINS')
                victory_message_surface = victory_font.render('LEFT SIDE WINS!',
                                                       True,
                                                       globals.player2.color_tuple)
                game_on = False  # The game loop will not run again
            if event.type == events.RIGHT_SIDE_WINS_TYPE:
                print('RIGHT SIDE WINS')
                victory_message_surface = victory_font.render('RIGHT SIDE WINS!',
                                                       True,
                                                       globals.player1.color_tuple)
                game_on = False  # The game loop will not run again



        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Update game models
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Shift game object locations
        # ---------------------------------------------
        globals.ball.move_to_next_frame()
        globals.player1.move_to_next_frame()
        globals.player2.move_to_next_frame()


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Draw
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Draw game objects
        # ---------------------------------------------

        globals.screen.fill(globals.BG_COLOR)
        pygame.draw.rect(globals.screen,
                         globals.player1.color_tuple,
                         globals.player1)
        pygame.draw.rect(globals.screen,
                         globals.player2.color_tuple,
                         globals.player2)
        pygame.draw.aaline(globals.screen,
                           globals.MIDLINE_COLOR_TUPLE,
                        (globals.SCREEN_WIDTH/2, 0),
                        (globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT))
        pygame.draw.ellipse(globals.screen,
                            globals.ball.color_tuple,
                            globals.ball.rect)


        # Draw score
        # ---------------------------------------------

        player1_score_surface = score_font.render(str(player1_score),
                                           True, globals.player1.color_tuple)
        player2_score_surface = score_font.render(str(player2_score),
                                        True, globals.player2.color_tuple)
        globals.screen.blit(player1_score_surface, (globals.SCREEN_WIDTH -80, 20))
        globals.screen.blit(player2_score_surface, (60, 20))

        if victory_message_surface is not None:
            globals.screen.blit(victory_message_surface,
                                (globals.SCREEN_WIDTH/2 - 400,
                                 globals.SCREEN_HEIGHT/2))

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Refresh display
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Update the window
        pygame.display.flip()
        clock.tick(globals.FRAME_RATE)


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Post-refresh
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Pause if point was scored
        if was_point_scored:
            pygame.time.delay(globals.PAUSE_ON_GOAL_MS)  # Pause game for 1000 ms
            was_point_scored = False

    # ==========================================================
    # Exiting
    # ==========================================================

    pygame.time.delay(globals.PAUSE_ON_WIN_MS)
    pygame.quit()


if __name__ == '__main__':
    main()
