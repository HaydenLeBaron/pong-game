# globals.py

"""This class contains the declarations and initializations for
global variables and constants."""

import pygame


def init():
    """The globals.init() function must be called at the
    beginning of __main__() (in the main file) to access
    these variables."""

    # Objects
    # -----------------------------------

    global player1;
    global player2;

    # Colors
    # -----------------------------------
    global DEF_TXT_COLOR_TUPLE; DEF_TXT_COLOR_TUPLE = (240, 240, 240)
    global BG_COLOR_TUPLE; BG_COLOR_TUPLE = (15, 15, 15)
    global BG_COLOR; BG_COLOR = pygame.Color(BG_COLOR_TUPLE[0],
                                             BG_COLOR_TUPLE[1],
                                             BG_COLOR_TUPLE[2])
    global MIDLINE_COLOR_TUPLE; MIDLINE_COLOR_TUPLE = (240, 240, 240)
    global P1_COLOR_TUPLE; P1_COLOR_TUPLE = (215, 40, 40)
    global P2_COLOR_TUPLE; P2_COLOR_TUPLE = (40, 40, 215)
    global BALL_COLOR_1; BALL_COLOR_1 = pygame.Color('yellow'),
    global BALL_COLOR_2; BALL_COLOR_2 = pygame.Color('green'),

    # Dimensions
    # -----------------------------------

    global SCREEN_WIDTH; SCREEN_WIDTH = 1280
    global SCREEN_HEIGHT; SCREEN_HEIGHT = 960
    global MENU_BUTTON_WIDTH; MENU_BUTTON_WIDTH = SCREEN_WIDTH - 80
    global MENU_BUTTON_HEIGHT; MENU_BUTTON_HEIGHT = 100


    # Positions
    # -----------------------------------
    # TODO: create constants for positions to make
    # graphical elements easily configuarable


    # Timing
    # -----------------------------------

    global FRAME_RATE; FRAME_RATE = 60
    global PAUSE_ON_GOAL_MS; PAUSE_ON_GOAL_MS = 1000
    global PAUSE_ON_WIN_MS; PAUSE_ON_WIN_MS = 3000


    # Other
    # -----------------------------------

    global DEF_BALL_SPEED; DEF_BALL_SPEED = 8

    # Ball speed is multiplied by this each volley
    global BALL_ACCELERATION; BALL_ACCELERATION = 1.2
    global DEF_PADDLE_SPEED; DEF_PADDLE_SPEED = 6
    global game_mode;  # == ('single_player' | 'pvp')
    global POINTS_TO_WIN; POINTS_TO_WIN = 3

    # Don't configure
    # -----------------------------------
   
    global click_flag; click_flag = False
