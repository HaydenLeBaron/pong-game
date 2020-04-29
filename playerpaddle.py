#
# playerpaddle.py
#

import globals
from paddle import _Paddle

class PlayerPaddle(_Paddle):

    def __init__(self, color_tuple, side):
        super().__init__(color_tuple, side)

    def move_to_next_frame(self):

        globals.player.rect.y += globals.player.y_speed  # Move player

        # Don't let player move off screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.rect.bottom = globals.SCREEN_HEIGHT
