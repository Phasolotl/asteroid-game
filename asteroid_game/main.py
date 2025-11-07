# Asteroid Game 101

import pygame as pg
from pygame import *

from asteroid_field import AsteroidField
from asteroid import Asteroid
from constants import *
from logger import log_state
from player import Player


def main():
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # group
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Asteroid Field

    asteroid_field = AsteroidField()

    # player position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    dt = 0

    while True:
        log_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        updatable.update(dt)

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

# end of code :3