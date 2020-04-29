#
# events.py
#

import pygame


def init():
    # Declare event types
    global TEST_EVENT_TYPE
    global LEFT_GOAL_SCORED_IN_TYPE  # Fires when ball touches left goal (right's point)
    global RIGHT_GOAL_SCORED_IN_TYPE # Fires when ball touches right goal (left's point)


    # Init event types
    TEST_EVENT_TYPE = pygame.USEREVENT + 1
    LEFT_GOAL_SCORED_IN_TYPE = pygame.USEREVENT + 2
    RIGHT_GOAL_SCORED_IN_TYPE = pygame.USEREVENT + 3



    # Declare events
    global test_event
    global left_goal_scored_in
    global right_goal_scored_in


    # Init events
    test_event = pygame.event.Event(TEST_EVENT_TYPE)
    left_goal_scored_in = pygame.event.Event(LEFT_GOAL_SCORED_IN_TYPE)
    right_goal_scored_in = pygame.event.Event(RIGHT_GOAL_SCORED_IN_TYPE)

    ###################################################
    # How to fire (post) events:
    #    pygame.event.post(test_event)
    #
    # How to handle test events
    # (in event handling part of loop in main.py):
    #    if event.type == TEST_EVENT_TYPE:
    #            pass
    ###################################################
