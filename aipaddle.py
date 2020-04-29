#
# aipaddle.py

"""This file contains a class for an AI-controlled paddle."""

import globals
from paddle import _Paddle
class AIPaddle(_Paddle):
    """Represents an AI-controlled paddle."""

    def __init__(self, color_tuple, side, target_ball):
        """Initializes a new AIPaddle"""

        super().__init__(color_tuple, side)
        self.y_speed = globals.DEF_PADDLE_SPEED
        self.target_ball = target_ball


    def move_to_next_frame(self):
        """Calculates the position of this AIPaddle as it
        will be drawn next frame."""

        # Move bot
        if self.rect.top < self.target_ball.rect.y:
            self.rect.top += self.y_speed
        if self.rect.bottom > self.target_ball.rect.y:
            self.rect.bottom -= self.y_speed

        # Don't let bot move off screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.rect.bottom = globals.SCREEN_HEIGHT
