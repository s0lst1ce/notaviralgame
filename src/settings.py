from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


WIDTH = 1366#1930
HEIGHT = 768#1080

# A collection of commonly used colors and their RGBA values
ALPHA = (0, 0, 0, 0)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 255)
YELLOW = (255, 255, 0, 255)
DARK_YELLOW = (246, 246, 67, 255)
CYAN = (0, 255, 255, 255)
MAGENTA = (255, 0, 255, 255)
ORANGE = (255, 165, 0, 255)
LIGHT_GREY = (178, 178, 178, 255)
DARK_GREY = (78, 78, 78, 255)
ORANGE_RED = (255, 69, 0, 255)
LIME_GREEN = (3, 125, 80)

# NODE
NODE_RADIUS = 50
PROXY_COLOR = ORANGE
MAX_LINKS = 4

#GEN
BORDER_OFFSET = 10
SPACING = (100, 300)

#BACKGROUND
RES = 20
SPEED = 0.3
BACKGROUND_COLOR = WHITE
