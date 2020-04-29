#
# paddle.py

"""This file contains a class representing a pong paddle."""

import globals
import pygame

class _Paddle:

    def __init__(self, color_tuple, side):
        """Initializes a new pong _Paddle
        with a given color tuple (0-255, 0-255, 0255)
        and a string $side ('right' | 'left') indicating which side
        of the court the paddle is on."""

        self.width = 15
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
        """Resets the position of this _Paddle to the middle of its
        correct $side ('right' | 'left')."""
        if side == 'right':
            self.rect.center = (globals.SCREEN_WIDTH - self.width,
                                globals.SCREEN_HEIGHT/2 - self.height/2)  # Move ball to center
        else:  # If side == 'left':
            self.rect.center = (self.width, globals.SCREEN_HEIGHT/2 - self.height/2)  # Move ball to center
