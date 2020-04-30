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

        # TODO: rename self.color_tuple to self.color and doc that
        # it takes a pygame.Color('colorname') object.
        self.color_tuple = color_tuple
        self.rect = pygame.Rect(globals.SCREEN_WIDTH/2 - diameter/2,
                                globals.SCREEN_HEIGHT/2 - diameter/2,
                                diameter, diameter)
        self.x_speed = x_speed
        self.y_speed = y_speed

        # Choose initial color based on movement direction
        if self.x_speed > 0:
            self.color_tuple = globals.BALL_COLOR_1
        else:
            self.color_tuple = globals.BALL_COLOR_2


    def move_to_next_frame(self, player1, player2):
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

        # Bounce balls on paddle collision, increase speed of ball and paddles
        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.x_speed *= -1*globals.BALL_ACCELERATION
            globals.FRAME_RATE *= globals.FRAME_RATE_MULTIPLIER

        # Change color based on movement direction
        if self.x_speed > 0:
            self.color_tuple = globals.BALL_COLOR_1
        else:
            self.color_tuple = globals.BALL_COLOR_2



    def restart(self):
        """Resets the ball to the middle and sends it in a new direction."""

        self.rect.center = (globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)  # Move ball to center
        self.x_speed = globals.DEF_BALL_SPEED * random.choice((1, -1))
        self.y_speed = globals.DEF_BALL_SPEED * random.choice((1, -1))

        # Change color based on movement direction
        if self.x_speed > 0:
            self.color_tuple = globals.BALL_COLOR_1
        else:
            self.color_tuple = globals.BALL_COLOR_2
