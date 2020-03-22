import pygame as pg
from settings import *

# init pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
game_surf = pg.Surface((WIDTH, HEIGHT))
game_surf.fill(WHITE)
clock = pg.time.Clock()
running = True


def start():
    """populate the game_surf"""
    global game_surf


def update():
    pass


def events():
    global running

    pressed_keys = pg.key.get_pressed()
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT or pressed_keys[pg.K_ESCAPE]:
            running = False


def render():
    global window
    global game_surf

    window.blit(game_surf, (0, 0))
    pg.display.update()


def main_loop():
    while running:
        clock.tick(60)
        events()
        update()
        render()


start()
main_loop()
