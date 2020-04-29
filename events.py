#
# events.py
#

import pygame


def init():
    # Declare event types
    global TEST_EVENT_TYPE


    # Init event types
    TEST_EVENT_TYPE = pygame.USEREVENT + 1


    # Declare events
    global test_event


    # Init events
    test_event = pygame.event.Event(TEST_EVENT_TYPE)

    ###################################################
    # How to fire (post) events:
    #    pygame.event.post(test_event)
    #
    # How to handle test events
    # (in event handling part of loop in main.py):
    #    if event.type == TEST_EVENT_TYPE:
    #            pass
    ###################################################
