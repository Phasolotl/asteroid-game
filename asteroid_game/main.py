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

    # group
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()

    # player position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    updatable.add(player)
    drawable.add(player)

    while True:
        log_state()
        dt = clock.tick(60) / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        updatable.update(dt)

        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)

        display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
