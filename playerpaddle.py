#
# playerpaddle.py

"""This file contains the class for a player-controlled pong paddle."""

import globals
from paddle import _Paddle

class PlayerPaddle(_Paddle):
    """A class representing a player-controlled Paddle.
    A PlayerPaddle is a _Paddle."""


    def __init__(self, color_tuple, side):
        """Initializes a new PlayerPaddle."""

        super().__init__(color_tuple, side)


    def move_to_next_frame(self):
        """Calculates the position of the PlayerPaddle as it
        will be drawn next frame."""

        self.rect.y += self.y_speed  # Move player

        # Don't let player move off screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.rect.bottom = globals.SCREEN_HEIGHT
