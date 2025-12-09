# Asteroid Game 101

import sys
import time as t
import pygame as pg
from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import *
from player import Player, Shot


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Groups
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
        self.score = 0
        self.running = True
        self.state = None

    def main_menu(self):
        self.state = MENU
        while self.running and self.state == MENU:
            print(self.state)

            self.screen.fill((10, 10, 10))
            title = MENU_FONT.render("ASTEROID SHOOTER 9000", True, (240, 240, 240))
            play = START_FONT.render("Press Enter to Start! Or Esc to Quit!", True, (180, 180, 180))
            self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)))
            self.screen.blit(play, play.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 80)))

            pg.display.flip()
            self.clock.tick(60)

            for events in pg.event.get():
                if events.type == pg.QUIT:
                    self.running = False
                    sys.exit()

                if self.state == MENU:
                    if events.type == pg.KEYDOWN and events.key in (pg.K_RETURN, pg.K_SPACE):
                        self.state = PLAYING
                        self.run()

                    if events.type == pg.MOUSEBUTTONDOWN:
                        self.state = PLAYING
                        self.run()

                    if events.type == pg.KEYDOWN and events.key == pg.K_ESCAPE:
                        self.running = False
                        break

    def run(self):
        while self.running and self.state == PLAYING:
            print(self.state)
            self.dt = self.clock.tick(60) / 1000

            for events in pg.event.get():
                if events.type == pg.QUIT:
                    self.state == MENU
                    sys.exit()

            self.updatable.update(self.dt)

            for ast in self.asteroids:
                if ast.collision(self.player):
                    print("Game over!")
                    t.sleep(1)
                    sys.exit()

            for ast in self.asteroids:
                for bullet in self.shots:
                    if bullet.collision(ast):
                        bullet.kill()
                        ast.split()
                        self.score += 100

            self.screen.fill((0,0,0))
            score_surface = SCORE_FONT.render(f'Score: {self.score}', True, (255,255,255))
            self.screen.blit(score_surface, (10,10))

            for bullet in self.shots:
                bullet.draw(self.screen)

            for obj in self.drawable:
                obj.draw(self.screen)

            pg.display.flip()

    def game_over(self):
        pass

if __name__ == '__main__':
    Game().main_menu()

# end of code :3