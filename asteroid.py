from circleshape import CircleShape
import pygame as pg
import random
from logger import log_event

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pg.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)

            for vel in (velocity1, velocity2):
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid.velocity = vel * 1.2

            return new_asteroid
