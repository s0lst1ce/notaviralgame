from random import randint, choice, random
from math import sin, cos, pi, sqrt

import pygame as pg
from settings import *
from nodes import Node
from link import Link

sign = lambda x: (1, -1)[x < 0]

def nodes(amount: tuple, spacing: tuple, bounds: tuple = (WIDTH, HEIGHT), size: int = NODE_RADIUS):
    #making first node
    nodes = []
    rects = []

    for i in range(randint(amount[0], amount[1])):
        loc = Point(randint(size, bounds[0]-size-15), randint(size, bounds[1]-size-15))
        rects.append(pg.Rect(loc.x- NODE_RADIUS, loc.y - NODE_RADIUS, 2* NODE_RADIUS, 2* NODE_RADIUS))
        nodes.append(Node(loc, size))

    print(rects[0])
    #normally not too many rects should be outside the game surface
    game_rect = pg.Rect(0, 0, WIDTH, HEIGHT)
    for rect in rects:
        if not game_rect.contains(rect):
            print("not inside " + rect)
            index = rects.index(rect)
            rects.pop(index)
            nodes.pop(index)

    #making sure no two node overlap
    for rect in rects:
        to_remove = rect.collidelistall(rects)
        #print(to_remove)
        for elem in to_remove:
            rects.pop(elem)
            nodes.pop(elem)

    
    return nodes