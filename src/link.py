import pygame as pg
from settings import *


class Link:
    """docstring for Link"""

    def __init__(self, *nodes, proxy=False):
        assert len(nodes) == 2, ValueError(
            "There must be exactly two nodes connected to a link."
        )
        self.nodes = nodes
        self.proxy = proxy
        for node in self.nodes:
            node.links.append(self)

    def get_color(self):
        if self.proxy:
            return PROXY_COLOR
        else:
            return BLUE

    def draw(self, dest):
        pg.draw.line(dest, self.get_color(), self.nodes[0].center, self.nodes[1].center)
