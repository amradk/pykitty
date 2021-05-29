import pygame
import random
from gameobject import GameObject
from car import Car
from carmanager import CarManager

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 600 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
TILE_WIDTH = 32
TILE_HEIGHT = 32

# class GameMapArea():
#     def __init__(self, pygame.rect, type):
#         """Manage maps"""
#         self.area_rect = rect
#         self.type = type

class GameMap():
    def __init__(self, screen, level):
        """Manage maps"""
        self.screen = screen
        self.level = level
        # groups for base tiles
        # there is should be react or sprite.Groups
        self.grp_sand = pygame.sprite.Group()
        self.grp_grass = pygame.sprite.Group()
        self.grp_road = pygame.sprite.Group()
        self.grp_ground = pygame.sprite.Group()
        self.grp_border = pygame.sprite.Group()
        self.grp_car = pygame.sprite.Group()
        self.car_points = []

    def load_ground_map(self):
        x=y=0 # координаты

        for row in self.level['grounds']: # вся строка
            for col in row: # каждый символ
                # grass
                if col == "g":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#39c936")
                    self.grp_grass.add(pf) 
                # sand
                if col == "s":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#e2f511")
                    self.grp_sand.add(pf) 
                # road
                if col == "r":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#575352")
                    self.grp_road.add(pf) 
                # ground
                if col == "G":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#26100a")
                    self.grp_ground.add(pf) 
                # border
                if col == "b":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#290505")
                    self.grp_border.add(pf)

                x += TILE_WIDTH #блоки платформы ставятся на ширине блоков
            y += TILE_HEIGHT    #то же самое и с высотой
            x = 0

    def load_object_map(self):
        x=y=0 # координаты

        for row in self.level['objects']: # вся строка
            for col in row: # каждый символ
                # the star point for car ganeration, forward x grown
                if col == "c":
                    cm = CarManager(self.screen, x, y, random.randrange(2,7), 1, 3)
                    cm.create_cars()    
                    #pf.set_color("#37bd3b")
                    self.car_points.append(cm)
                if col == "C":
                    cm = CarManager(self.screen, x, y, random.randrange(1,6), -1, 3)
                    cm.create_cars()    
                    #pf.set_color("#37bd3b")
                    self.car_points.append(cm)

                x += TILE_WIDTH #блоки платформы ставятся на ширине блоков
            y += TILE_HEIGHT    #то же самое и с высотой
            x = 0

    def load_map(self):
        self.load_ground_map()
        self.load_object_map()

    def update(self):
        self.grp_sand.update()
        self.grp_grass.update()
        self.grp_road.update()
        self.grp_ground.update()
        self.grp_border.update()
        self.grp_car.update()
        for cm in self.car_points:
            cm.update()

    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        #self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.grp_sand.draw(self.screen)
        self.grp_grass.draw(self.screen)
        self.grp_road.draw(self.screen)
        self.grp_ground.draw(self.screen)
        self.grp_border.draw(self.screen)
        self.grp_car.draw(self.screen)
        for cm in self.car_points:
            cm.draw()