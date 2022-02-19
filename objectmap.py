import pygame
import random
from const import *
from carmanager import CarManager
from gamemap import GameMap

class ObjectMap(GameMap):
    def __init__(self, screen, level):
        """Manage maps"""
        self.screen = screen
        self.level = level
        self.grp_car = pygame.sprite.Group()
        self.car_points = []

    def load_map(self):
        x=y=0 # координаты

        for row in self.level['objects']: # вся строка
            for col in row: # каждый символ
                # the star point for car ganeration, forward x grown
                if col == "c":
                    cm = CarManager(self.screen, 0 - 480, y, random.randrange(2,7), 1, 3)
                    cm.create_cars()
                    #pf.set_color("#37bd3b")
                    self.car_points.append(cm)
                if col == "C":
                    cm = CarManager(self.screen, WIN_WIDTH, y, random.randrange(1,6), -1, 3)
                    cm.create_cars()
                    #pf.set_color("#37bd3b")
                    self.car_points.append(cm)

                x += TILE_WIDTH #блоки платформы ставятся на ширине блоков
            y += TILE_HEIGHT    #то же самое и с высотой
            x = 0

    def update(self):
        for cm in self.car_points:
            cm.update()

    def draw(self):
        for cm in self.car_points:
            cm.draw()

    def check_collision(self):
        pass
