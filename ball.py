#
# ball.py
#
#

import globals
import events
import pygame
import random

class Ball:

    def __init__(self, diameter=30, color_tuple=(30, 30, 0), x_speed=7, y_speed=7):

        self.diameter = diameter
        self.color_tuple = color_tuple
        self.rect = pygame.Rect(globals.SCREEN_WIDTH/2 - diameter/2,
                                globals.SCREEN_HEIGHT/2 - diameter/2,
                                diameter, diameter)
        self.x_speed = x_speed
        self.y_speed = y_speed


    def move_to_next_frame(self):

        # Move ball
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Bounce balls on wall collision
        if self.rect.top <= 0 or self.rect.bottom >= globals.SCREEN_HEIGHT:
           self.y_speed *= -1
           pygame.event.post(events.test_event)  # DEBUG: POST TEST EVENT

        # If the ball touches the left-side goal
        if self.rect.left <= 0:
            pygame.event.post(events.left_goal_scored_in)

        # If the ball touches the right-side goal
        if self.rect.right >= globals.SCREEN_WIDTH:
            pygame.event.post(events.right_goal_scored_in)


        # If the ball hits the goal, reset ball and paddle positions
        if self.rect.left <= 0 or self.rect.right >= globals.SCREEN_WIDTH:
            globals.player.reset_position('right')
            globals.bot.reset_position('left')
            self.restart()
            pygame.time.delay(1000)  # Pause game for 1000 ms


        # Bounce balls on paddle collision
        if self.rect.colliderect(globals.player) or self.rect.colliderect(globals.bot):
            self.x_speed *= -1

    def restart(self):

        self.rect.center = (globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)  # Move ball to center
        self.x_speed *= random.choice((1, -1))
        self.y_speed *= random.choice((1, -1))
