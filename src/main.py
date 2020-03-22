import pygame as pg
from settings import *
from nodes import Node
from link import Link
import gen as gen

# init pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
game_surf = pg.Surface((WIDTH, HEIGHT))
game_surf.fill(WHITE)
clock = pg.time.Clock()
running = True




"""
node1 = Node(Point(100, 100), NODE_RADIUS)
node2 = Node(Point(300, 300), NODE_RADIUS)
link1 = Link(node1, node2)"""

# this dict is useful because we need to draw the links before the nodes or it will look wrong (line over circle)
entities = {"nodes": [], "links": []}


def start():
    """populate the game_surf"""
    global game_surf
    global entities

    entities["nodes"] = gen.nodes((8, 10), SPACING)


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

    # drawing game content
    for link in entities["links"]:
        link.draw(game_surf)
    for node in entities["nodes"]:
        node.draw(game_surf)

    # updating this
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
