import pygame as pg
from settings import *

surf_infected = pg.Surface((NODE_RADIUS, NODE_RADIUS), color=RED)
surf_sain = pg.Surface((NODE_RADIUS, NODE_RADIUS), color=BLUE)

node_surfs = {
    True: surf_sain,
    False: surf_infected,
}


class Node:
    """docstring for Node object"""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

        self.infected = False
        self.links = []

        self.surf = node_surfs[self.infected]

    def draw(self, dest):
        dest.blit(self.surf, self.center.x, self.center.y)
