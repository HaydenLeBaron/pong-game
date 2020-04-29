# globals.py

"""This class contains the declarations and initializations for
global variables and constants."""

import pygame


def init():
    """The globals.init() function must be called at the
    beginning of __main__() (in the main file) to access
    these variables."""

    #Declare constants
    global BG_COLOR
    global MIDLINE_COLOR_TUPLE
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global FRAME_RATE
    global POINTS_TO_WIN
    global PAUSE_ON_GOAL_MS
    global PAUSE_ON_WIN_MS
    global DEF_BALL_SPEED
    global DEF_PADDLE_SPEED

    # Declare non-constants
    global screen
    global game_mode

    # Declare global game objects
    global ball
    global player1
    global player2

    # Initialize constants
    BG_COLOR = pygame.Color('black')
    MIDLINE_COLOR_TUPLE = (255, 255, 255)
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 960
    FRAME_RATE = 60
    POINTS_TO_WIN = 5
    PAUSE_ON_GOAL_MS = 1000
    PAUSE_ON_WIN_MS = 3000
    DEF_BALL_SPEED = 10
    DEF_PADDLE_SPEED = 10

    # Initialize non-constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_mode = 'pvp'  # == ('single_player' | 'pvp')
