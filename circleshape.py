import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass # will be overwritten

    def update(self, dt):
        pass # will be overwritten

    def collision(self, other):
        r1 = self.radius
        r2 = other.radius
        distance = pygame.math.Vector2.distance_to(self.position, other.position)

        if (r1 + r2) >= distance:
            return True
        else:
            return False
