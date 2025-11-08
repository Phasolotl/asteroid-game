# Asteroid Game 101

import sys
import time as t
import pygame as pg
from pygame import *

from asteroid_field import AsteroidField
from asteroid import Asteroid
from constants import *
from logger import log_state, log_event
from player import Player, Shot


def main():
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # group
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, shots)

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

        for ast in asteroids:
            if ast.collision(player):
                log_event("player_hit")
                print("Game over!")
                t.sleep(1)
                sys.exit()

        screen.fill((0,0,0))

        for bullet in shots:
            bullet.draw(screen)

        for obj in drawable:
            obj.draw(screen)

        display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

# end of code :3