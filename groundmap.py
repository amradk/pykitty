import pygame
from const import *
from gameobject import GameObject
from gamemap import GameMap

class GroundMap(GameMap):
    def __init__(self, screen, level):
        """Manage ground maps"""
        self.screen = screen
        self.level = level
        # groups for base tiles
        # there is should be react or sprite.Groups
        self.grp_sand = pygame.sprite.Group()
        self.grp_grass = pygame.sprite.Group()
        self.grp_road = pygame.sprite.Group()
        self.grp_ground = pygame.sprite.Group()
        self.grp_border = pygame.sprite.Group()

    def load_map(self):
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
        self.grp_sand.update()
        self.grp_grass.update()
        self.grp_road.update()
        self.grp_ground.update()
        self.grp_border.update()


    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        #self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.grp_sand.draw(self.screen)
        self.grp_grass.draw(self.screen)
        self.grp_road.draw(self.screen)
        self.grp_ground.draw(self.screen)
        self.grp_border.draw(self.screen)

    def check_collision(self, player_group):
        # если игрок пересекается с несколькими спрайтами то применяем наибольший штраф
        collisions = []
        if pygame.sprite.groupcollide(player_group, self.grp_sand, False, False):
            collisions.append('sand')
        if pygame.sprite.groupcollide(player_group, self.grp_grass, False, False):
            collisions.append('grass')
        if pygame.sprite.groupcollide(player_group, self.grp_road, False, False):
            collisions.append('road')
        if pygame.sprite.groupcollide(player_group, self.grp_ground, False, False):
            collisions.append('ground')
        if pygame.sprite.groupcollide(player_group, self.grp_border, False, False):
            collisions.append('border')

        return collisions
