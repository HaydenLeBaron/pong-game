#
# aipaddle.py
#

import globals
from paddle import _Paddle
class AIPaddle(_Paddle):

    def __init__(self, color_tuple, side, target_ball):
        super().__init__(color_tuple, side)
        self.y_speed = 7
        self.target_ball = target_ball

    def move_to_next_frame(self):

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
