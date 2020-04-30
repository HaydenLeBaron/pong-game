# globals.py

"""This class contains the declarations and initializations for
global variables and constants."""

import pygame


def init():
    """The globals.init() function must be called at the
    beginning of __main__() (in the main file) to access
    these variables."""


    # Colors
    # -----------------------------------

    global BG_COLOR; BG_COLOR = pygame.Color(15, 15, 15)
    global MIDLINE_COLOR_TUPLE; MIDLINE_COLOR_TUPLE = (255, 255, 255)
    global P1_COLOR_TUPLE; P1_COLOR_TUPLE = (215, 40, 40)
    global P2_COLOR_TUPLE; P2_COLOR_TUPLE = (40, 40, 215)


    # Dimensions
    # -----------------------------------

    global SCREEN_WIDTH; SCREEN_WIDTH = 1280
    global SCREEN_HEIGHT; SCREEN_HEIGHT = 960


    # Timing
    # -----------------------------------

    global FRAME_RATE; FRAME_RATE = 60
    global PAUSE_ON_GOAL_MS; PAUSE_ON_GOAL_MS = 1000
    global PAUSE_ON_WIN_MS; PAUSE_ON_WIN_MS = 3000


    # Other
    # -----------------------------------

    global DEF_BALL_SPEED; DEF_BALL_SPEED = 9
    global POINTS_TO_WIN; POINTS_TO_WIN = 2
    global DEF_PADDLE_SPEED; DEF_PADDLE_SPEED = 9
    global game_mode; game_mode = 'pvp'  # == ('single_player' | 'pvp')


    # Don't configure
    # -----------------------------------
   
    global click_flag; click_flag = False
