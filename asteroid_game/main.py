import pygame as pg
from pygame import *

from constants import *
from logger import log_state

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        Surface.fill(screen, (0,0,0))
        display.flip()

if __name__ == "__main__":
    main()
