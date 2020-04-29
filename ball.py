#
# ball.py

"""This file contains a class for a ball."""


import globals
import events
import pygame
import random

class Ball:
    """Represents a ball."""

    def __init__(self, diameter, color_tuple, x_speed, y_speed):
        """Initializes a new ball with a given diameter, color, and speed."""

        self.diameter = diameter
        self.color_tuple = color_tuple
        self.rect = pygame.Rect(globals.SCREEN_WIDTH/2 - diameter/2,
                                globals.SCREEN_HEIGHT/2 - diameter/2,
                                diameter, diameter)
        self.x_speed = x_speed
        self.y_speed = y_speed


    def move_to_next_frame(self):
        """Calculates the position of the ball as it
        will be drawn next frame."""

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

        # Bounce balls on paddle collision
        if self.rect.colliderect(globals.player1) or self.rect.colliderect(globals.player2):
            self.x_speed *= -1

    def restart(self):
        """Resets the ball to the middle and sends it in a new direction."""

        self.rect.center = (globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)  # Move ball to center
        self.x_speed *= random.choice((1, -1))
        self.y_speed *= random.choice((1, -1))
