import pygame
import random
from const import *
from gameobject import GameObject
from carmanager import CarManager
from gamemap import GameMap
from hmoveobject import HMoveObject

class ObjectMap(GameMap):
    def __init__(self, screen, level):
        """Manage maps"""
        self.screen = screen
        self.level = level
        self.grp_car = pygame.sprite.Group()
        self.car_points = []
        self.grp_fin = pygame.sprite.Group()
        self.grp_dog = pygame.sprite.Group()

    def load_map(self):
        x=y=0 # координаты

        for row in self.level['objects']: # вся строка
            for col in row: # каждый символ
                # the star point for car ganeration, forward x grown
                if col == "c":
                    cm = CarManager(self.screen, 0 - 480, y, random.randrange(2,7), 1, 3)
                    cm.create_cars()
                    self.car_points.append(cm)
                if col == "C":
                    cm = CarManager(self.screen, WIN_WIDTH, y, random.randrange(1,6), -1, 3)
                    cm.create_cars()
                    self.car_points.append(cm)
                if col == 'F':
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color(pygame.Color(MAGENTA))
                    self.grp_fin.add(pf)
                # собачки
                if col == 'd':
                    print('Process dog')
                    #создаем блок, заливаем его цветом и рисеум его
                    dog = HMoveObject(pygame.Color(BROWN), 2, x, y, TILE_WIDTH, TILE_HEIGHT)
                    dog.set_behaviour({'move_mode' : 'patrol', 'move_radius' : 3, 'move_direction' : 'direct'})
                    self.grp_dog.add(dog)

                x += TILE_WIDTH #блоки платформы ставятся на ширине блоков
            y += TILE_HEIGHT    #то же самое и с высотой
            x = 0

    def update(self):
        self.grp_dog.update()
        for cm in self.car_points:
            cm.update()

    def draw(self):
        for cm in self.car_points:
            cm.draw()
        self.grp_fin.draw(self.screen)
        self.grp_dog.draw(self.screen)

    def check_collision(self, player_group):
        collisions = []
        for cm in self.car_points:
            if cm.check_collisions(player_group):
                collisions.append('cars')
        if pygame.sprite.groupcollide(player_group, self.grp_fin, False, False):
            collisions.append('fin')

        return collisions
