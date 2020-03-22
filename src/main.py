import pygame as pgm
from settings import *

#init pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
game_surf = pg.Surface((WIDTH, HEIGHT))
game_surf.fill(WHITE)
clock = pg.time.Clock()
running = True


def start():
    """populate the game_surf"""
    pass


def update():
    pass

def events():
    global running

    pressed_keys = pg.key.get_pressed()
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT pr pressed_keys[pg.K_ESCAPE]:
            running = False


def render():
    pass


def main_loop():
    pass