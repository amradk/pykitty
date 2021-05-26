import pygame
from gameobject import GameObject
from car import Car

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
    def __init__(self, level):
        """Manage maps"""
        self.level = level
        # groups for base tiles
        # there is should be react or sprite.Groups
        self.grp_sand = pygame.sprite.Group()
        self.grp_grass = pygame.sprite.Group()
        self.grp_road = pygame.sprite.Group()
        self.grp_ground = pygame.sprite.Group()
        self.grp_border = pygame.sprite.Group()
        self.grp_car = pygame.sprite.Group()

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
                    pf = Car("#37bd3b", 1, x, y)    
                    #pf.set_color("#37bd3b")
                    self.grp_car.add(pf)
                if col == "C":
                    pf = Car("#1945e3", -2, x, y)    
                    #pf.set_color("#1945e3")
                    self.grp_car.add(pf)

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

    def draw(self, screen):
        # При каждом проходе цикла перерисовывается экран.
        #self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.grp_sand.draw(screen)
        self.grp_grass.draw(screen)
        self.grp_road.draw(screen)
        self.grp_ground.draw(screen)
        self.grp_border.draw(screen)
        self.grp_car.draw(screen)