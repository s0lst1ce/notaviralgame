import pygame as pg
from settings import *

surf_infected = pg.Surface((2*NODE_RADIUS, 2*NODE_RADIUS))
surf_infected.set_colorkey(BACKGROUND_COLOR)
surf_infected.fill(BACKGROUND_COLOR)
surf_sain = surf_infected.copy()

pg.draw.circle(surf_infected, (254, 254, 254), (NODE_RADIUS, NODE_RADIUS), NODE_RADIUS)
pg.draw.circle(surf_sain, (254, 254, 254), (NODE_RADIUS, NODE_RADIUS), NODE_RADIUS)
pg.draw.circle(surf_infected, RED, (NODE_RADIUS, NODE_RADIUS), NODE_RADIUS-5)
pg.draw.circle(surf_sain, BLUE, (NODE_RADIUS, NODE_RADIUS), NODE_RADIUS-5)

node_surfs = {
    False: surf_sain,
    True: surf_infected,
}


class Node:
    """docstring for Node object"""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

        self.infected = False
        self.links = []

        self.make_surf()

    def draw(self, dest):
        dest.blit(self.surf, (self.center.x - self.radius, self.center.y- self.radius))

    def make_surf(self):
        self.surf = node_surfs[self.infected]
