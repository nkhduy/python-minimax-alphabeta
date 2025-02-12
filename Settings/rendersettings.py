import Settings.gamesettings as game_settings

# FPS
FPS = 60

# RGB COLOR
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (195, 195, 195)
COLOR_WOOD_BROWN = (208, 161, 115)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_WHITE_VANILLA = (244, 240, 220)
COLOR_BRIGHT_YELLOW = (251, 230, 91)
COLOR_CYAN = (57, 183, 237)
COLOR_DARK_GREEN = (0, 100, 0)
COLOR_DARK_PINK = (130, 0, 130)
COLOR_PINK = (255, 0, 90)
COLOR_GREEN = (0, 180, 0)
COLOR_ORANGE = (255, 115, 0)
COLOR_DARK_RED = (142, 21, 21)
COLOR_DEEP_SKY_BLUE = (0, 155, 255)
COLOR_BLUE_VIOLET = (138, 43, 226)
COLOR_PURPLE = (128, 0, 128)
PURPLE = (142, 101, 132)
LIGHT_PINK = (255, 203, 192)  # Color for 'O'
SOFT_YELLOW = (242, 214, 143) # Color for 'X'

# SET X AND O COLOR
X_COLOR = SOFT_YELLOW
O_COLOR = LIGHT_PINK
O_LAST_MOVE_COLOR = COLOR_BLUE
X_LAST_MOVE_COLOR = COLOR_BLUE

def get_last_move_color(player):
    if (player == game_settings.O):
        return O_LAST_MOVE_COLOR
    if (player == game_settings.X):
        return X_LAST_MOVE_COLOR

# BORDER
BORDER_SIZE = 30

# INFO TEXT
INFO_TEXT_FONT_SIZE = 20

HOME_INFO_TEXT = "HOME"
NEW_GAME_INFO_TEXT = "PRESS \"NEW GAME\" TO RESET"
HUMAN_TURN_INFO_TEXT = "YOUR TURN"
COM_TURN_INFO_TEXT = "AI TURN"
HUMAN_WIN_INFO_TEXT = "YOU WIN!"
COM_WIN_INFO_TEXT = "AI WIN!"
DRAW_INFO_TEXT = "DRAW!"

# BOARD
SQUARE_SIZE = 35 

CENTER_CIRCLE_RADIUS = 8

BOARD_WIDTH = game_settings.BOARD_COL_COUNT * SQUARE_SIZE
BOARD_HEIGHT = game_settings.BOARD_ROW_COUNT * SQUARE_SIZE

BOARD_POS_X_MIN = BORDER_SIZE
BOARD_POS_Y_MIN = BORDER_SIZE + INFO_TEXT_FONT_SIZE + BORDER_SIZE
BOARD_POS_X_MAX = BOARD_POS_X_MIN + BOARD_WIDTH
BOARD_POS_Y_MAX = BOARD_POS_Y_MIN + BOARD_HEIGHT

BOARD_COLOR = PURPLE
BOARD_LINE_WIDTH = 2

# BUTTON
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 45
BUTTON_COLOR = COLOR_GREY
BUTTON_TEXT_COLOR = COLOR_WHITE
BUTTON_TEXT_FONT_SIZE = 20
BUTTON_SPACING = 8

# WINDOW
WINDOW_WIDTH = BORDER_SIZE + BOARD_WIDTH + BORDER_SIZE
WINDOW_HEIGHT = BORDER_SIZE + INFO_TEXT_FONT_SIZE + BORDER_SIZE + BOARD_HEIGHT + BORDER_SIZE + BUTTON_HEIGHT + BORDER_SIZE*2
WINDOW_TITLE = 'VS AI'

# CELL
O_CELL_BORDER = 4
O_RADIUS = SQUARE_SIZE/2
O_LINE_THICKNESS = 4

X_CELL_BORDER = 6
X_LINE_THICKNESS = 6


# NEW GAME BUTTON

NEW_GAME_BUTTON_POS_X_MIN = BORDER_SIZE + (BOARD_WIDTH - BUTTON_WIDTH)/2
NEW_GAME_BUTTON_POS_X_MAX = NEW_GAME_BUTTON_POS_X_MIN + BUTTON_WIDTH
NEW_GAME_BUTTON_POS_Y_MIN = BORDER_SIZE*2 + INFO_TEXT_FONT_SIZE + BOARD_HEIGHT + BORDER_SIZE
NEW_GAME_BUTTON_POS_Y_MAX = NEW_GAME_BUTTON_POS_Y_MIN + BUTTON_HEIGHT

NEW_GAME_BUTTON_POS = (NEW_GAME_BUTTON_POS_X_MIN, NEW_GAME_BUTTON_POS_Y_MIN)

# HOME BUTTON

HOME_BUTTON_POS_X_MIN = NEW_GAME_BUTTON_POS_X_MIN
HOME_BUTTON_POS_X_MAX = NEW_GAME_BUTTON_POS_X_MAX
HOME_BUTTON_POS_Y_MIN = NEW_GAME_BUTTON_POS_Y_MAX + BUTTON_SPACING
HOME_BUTTON_POS_Y_MAX = HOME_BUTTON_POS_Y_MIN + BUTTON_HEIGHT

HOME_BUTTON_POS = (HOME_BUTTON_POS_X_MIN, HOME_BUTTON_POS_Y_MIN)