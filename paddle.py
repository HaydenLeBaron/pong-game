#
# paddle.py
#

import globals
import pygame

class _Paddle:
    def __init__(self, color_tuple, side):
        # side -- a string (either 'right' or 'left'), indicating what side the paddle is on (default: right)


        self.width = 20
        self.height = 150
        self.color_tuple = color_tuple
        self.y_speed = 0

        if side == 'right':
            self.rect = pygame.Rect(globals.SCREEN_WIDTH - 20,
                                    globals.SCREEN_HEIGHT/2 - self.height/2,
                                    self.width, self.height)
        else:  # If side == 'left':
            self.rect = pygame.Rect(10,
                                    globals.SCREEN_HEIGHT/2 - self.height/2,
                                    self.width, self.height)

    def reset_position(self, side):
        if side == 'right':
            self.rect.center = (globals.SCREEN_WIDTH - 20,
                                globals.SCREEN_HEIGHT/2 - self.height/2)  # Move ball to center
        else:  # If side == 'left':
            self.rect.center = (10, globals.SCREEN_HEIGHT/2 - self.height/2)  # Move ball to center
