import pygame


class GameMapArea():
    def __init__(self, pygame.rect, type):
        """Manage maps"""
        self.area_rect = rect
        self.type = type



class GameMap():
    def __init__(self, level):
        """Manage maps"""
        self.level = level
        # groups for base tiles
        # there is should be react or sprite.Groups
        self.grp_sand = []
        self.grp_grass = []
        self.grp_road = []
        self.grp_ground = []
        self.grp_border = []

    def load_map(self):
        x=y=0 # координаты
        grass_group = pygame.sprite.Group()
        sand_group = pygame.sprite.Group()
        road_group =pygame.sprite.Group()
        ground_group = pygame.sprite.Group()
        border_group = pygame.sprite.Group()

        for row in level: # вся строка
            for col in row: # каждый символ
                # grass
                if col == "g":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(grass_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#39c936")
                    grass_group.add(pf) 
                # sand
                if col == "s":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(sand_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#e2f511")
                    sand_group.add(pf) 
                # road
                if col == "r":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(athphalt_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#575352")
                    road_group.add(pf)
                # the star point for car ganeration, forward x grown
                if col == "c":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(athphalt_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#575352")
                    road_group.add(pf)
                # the star point for car ganeration, backward x decrease
                if col == "C":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(athphalt_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#575352")
                    road_group.add(pf) 
                # ground
                if col == "G":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(ground_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#26100a")
                    ground_group.add(pf) 
                # border
                if col == "b":
                    #создаем блок, заливаем его цветом и рисеум его
                    pf = GameObject(border_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                    pf.set_color("#290505")
                    border_group.add(pf)

                x += TILE_WIDTH #блоки платформы ставятся на ширине блоков
            y += TILE_HEIGHT    #то же самое и с высотой
            x = 0
        
        self.grp_sand = [sand_group]
        self.grp_grass = [grass_group]
        self.grp_road = [road_group]
        self.grp_ground = [ground_group]
        self.grp_border = [border_group]

    def set_color(self, color):
        self.color = color
        self.image.fill(pygame.Color(color))