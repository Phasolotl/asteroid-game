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


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # group
        self.updatable = pg.sprite.Group()
        self.drawable = pg.sprite.Group()
        self.asteroids = pg.sprite.Group()
        self.shots = pg.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable
        Shot.containers = (self.updatable, self.drawable, self.shots)

        # Asteroid Field

        self.asteroid_field = AsteroidField()

        # player position
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        self.player = Player(x, y)

        self.dt = 0

    def run(self):
        while True:
            log_state()

            for events in pg.event.get():
                if events.type == pg.QUIT:
                    return

            self.updatable.update(self.dt)

            for ast in self.asteroids:
                if ast.collision(self.player):
                    log_event("player_hit")
                    print("Game over!")
                    t.sleep(1)
                    sys.exit()

            for ast in self.asteroids:
                for bullet in self.shots:
                    if bullet.collision(ast):
                        log_event("asteroid_shot")
                        bullet.kill()
                        ast.split()

            self.screen.fill((0,0,0))

            for bullet in self.shots:
                bullet.draw(self.screen)

            for obj in self.drawable:
                obj.draw(self.screen)

            display.flip()

            self.dt = self.clock.tick(60) / 1000

Game().run()

# end of code :3