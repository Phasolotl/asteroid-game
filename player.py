import pygame as pg

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, \
    PLAYER_SHOOT_COOLDOWN


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360

    def update(self, dt):
        keys = pg.key.get_pressed()
        self.cooldown -= dt

        if keys[pg.K_a]:
            self.rotate(-dt)
        if keys[pg.K_d]:
            self.rotate(dt)
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-dt)
        if keys[pg.K_SPACE]:
            self.shoot()

        screen_rect = pg.display.get_surface().get_rect()
        r = getattr(self, "radius", 0)
        self.position.x = max(screen_rect.left + r, min(self.position.x, screen_rect.right - r))
        self.position.y = max(screen_rect.top + r, min(self.position.y, screen_rect.bottom - r))

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position, self.velocity)

        distance = pg.Vector2(0,1).rotate(self.rotation)
        shot.velocity = distance * PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pg.Vector2(x, 0)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
