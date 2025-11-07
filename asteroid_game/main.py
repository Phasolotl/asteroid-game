import pygame as pg
from pygame import *
from constants import *
from logger import log_state
from player import Player


def main():
    pg.init()
    clock = pg.time.Clock()
    dt = 0
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # player position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        log_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        Surface.fill(screen, (0,0,0))
        ######################################
        player.draw(screen)
        player.update(dt)
        ######################################
        display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
