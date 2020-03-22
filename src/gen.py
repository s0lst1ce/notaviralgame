from random import randint, choice, random
from math import sin, cos, pi, sqrt

import pygame as pg
from settings import *
from nodes import Node
from link import Link

sign = lambda x: (1, -1)[x < 0]

def nodes(amount: tuple, spacing: tuple, bounds: tuple = (WIDTH, HEIGHT), size: int = NODE_RADIUS):
    #making first node
    nodes = [Node(Point(randint(size, bounds[0]-size), randint(size, bounds[1]-size)), size)]

    angle_inverter = 1
    for i in range(randint(amount[0], amount[1])):
        loc = nodes[-1].center #starting from the center of the last node

        angle = 2 * pi * random() * angle_inverter #random angle in radian
        rel_pos = Point(int(cos(angle) * size), int(sin(angle) * size)) #putting point on the border of the circle

        rel_offset = randint(*spacing)

        loc = Point(loc.x + rel_pos.x + sign(rel_pos.x) * rel_offset, loc.y + rel_pos.y + sign(rel_pos.y) * rel_offset)

        nodes.append(Node(loc, size))
        angle_inverter = angle_inverter * -1


    #normally not too many rects should be outside the game surface

    return nodes