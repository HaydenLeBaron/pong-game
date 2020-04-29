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


    # General setup
    # -----------------------------------

    globals.init()
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Pong')


    # Game Objects
    # -----------------------------------

    globals.ball = Ball(30, pygame.Color('yellow'),
                7 * random.choice((1, -1)),
                7 * random.choice((1, -1)))
    globals.player = PlayerPaddle((0, 0, 240), 'right')
    globals.bot = AIPaddle((240, 0, 0), 'left', globals.ball)




    # Game loop
    # -----------------------------------


    gamefont = pygame.font.SysFont('Helvetica', 48, bold=True, italic=False)
    textsurface = gamefont.render('Hello world', True, (0,0,255))

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
            EVENT_TYPE1 = pygame.USEREVENT + 1
            test_event = pygame.event.Event(EVENT_TYPE1)
            pygame.event.post(test_event)
            # Handle test events
            if event.type == EVENT_TYPE1:
                print('YAY')
                pygame.draw.ellipse(globals.screen,
                                    (20, 30, 50),
                                    pygame.Rect(random.randint(100, 500),
                                         random.randint(100, 500) , 30, 40))

            #============================================
            # Handle goal score events
           

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


        # Draw score  # TODO: BOOKMARK NOTE: I should be using events
        globals.screen.blit(textsurface, (200, 400))

        # Updating the window
        pygame.display.flip()
        clock.tick(globals.FRAME_RATE)


if __name__ == '__main__':
    main()
