import pygame as pg
import os
from math import sin
from random import randint
from settings import *

# init pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
game_surf = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA).convert_alpha()
clock = pg.time.Clock()
running = True

fxsurf = pg.Surface((WIDTH-70, HEIGHT-70)).convert()
fxsurf.set_alpha(128)

from nodes import Node
from link import Link
import gen as gen

#audio
pg.mixer.init()
musics = []
for music in os.listdir(os.path.join("music")):
    print(os.path.join("music", music))
    musics.append(pg.mixer.music.load(os.path.join("music", music)))
    #pg.mixer.music.queue(musics[-1])


# this dict is useful because we need to draw the links before the nodes or it will look wrong (line over circle)
entities = {"nodes": [], "links": []}

node_blacklist = list()

# increasing variable for the animation of background
background_increase = 0

# a flag to check if gameplay has started
first_infection = False

def start():
    """populate the game_surf"""
    global game_surf
    global entities

    entities["nodes"] = gen.nodes((12, 20), SPACING)
    entities["links"] = gen.links(*entities["nodes"])


def update():
    pass


def events():
    global running
    global first_infection
    global node_blacklist

    pressed_keys = pg.key.get_pressed()
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT or pressed_keys[pg.K_ESCAPE]:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = pg.mouse.get_pos()
            if event.button == 1:
                #Gameplay has started
                if first_infection:
                    for node in entities["nodes"]:
                        if node not in node_blacklist:
                            if (mx - node.center[0]) ** 2 + (my - node.center[1]) ** 2 < node.radius ** 2:
                                #Check for neighbours
                                infecteds = list()
                                for link in node.links:
                                    for n in link.nodes:
                                        if n.infected and n not in infecteds: infecteds.append(n)

                                if len(infecteds) > 0:
                                    # TODO: PROBABILTY

                                    # 20% placeholder
                                    if randint(1, 2) == 1:
                                        node.infected = True
                                        node.make_surf()
                                    else:
                                        node_blacklist.append(node)


                #Gameplay hasn't started
                else:
                    for node in entities["nodes"]:
                        if (mx - node.center[0]) ** 2 + (my - node.center[1]) ** 2 < node.radius ** 2:
                            node.infected = True
                            node.make_surf()
                            first_infection = True
                            break

        #loop music
        if not pg.mixer.music.get_busy():
            pg.mixer.music.rewind()



def render():
    global window
    global game_surf
    global background_increase

    window.fill((52, 171, 235))
    background_increase -= SPEED
    a = 0
    for y in range((HEIGHT//RES)+1):
        a+=1
        for x in range((WIDTH//RES)+1):
            pg.draw.circle(window, (140, 215, 255), (x*RES, y*RES), (sin(x+a+background_increase)+2)*1.5)

    window.blit(fxsurf, (35, 35))

    # drawing game content
    for link in entities["links"]:
        link.draw(game_surf)
    for node in entities["nodes"]:
        node.draw(game_surf)

    # updating this
    window.blit(game_surf, (0, 0))
    pg.display.update()


def main_loop():
    pg.mixer.music.play(-1)
    while running:
        clock.tick(60)
        events()
        update()
        render()


start()
main_loop()
