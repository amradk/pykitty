import pygame
from state import State
import sys
from player import Player
from map import GameMap
from hud import Hud
from gameobject import GameObject
from random import randrange


class GameState(State):

    def __init__(self, screen, state_manager):
        super(State, self).__init__()
        self.state_manager = state_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        # define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.BAR_LENGTH = 100
        self.BAR_HEIGHT = 10
        # Группы для спрайтов
        self.grp_player = pygame.sprite.Group()
        self.grp_cars = pygame.sprite.Group()
        self.grp_sand = pygame.sprite.Group()
        self.grp_grass = pygame.sprite.Group()
        self.grp_road = pygame.sprite.Group()
        self.grp_ground = pygame.sprite.Group()
        self.grp_border = pygame.sprite.Group()

        self.pl = None
        self.map = None

    def draw_hud(self):
        pass

    def init(self):
        self.screen.fill((0, 0, 255))
        self.scores = 0
        #ДК очищаем игры
        self.grp_player.empty()
        self.grp_cars.empty()
        self.grp_sand.empty()
        self.grp_grass.empty()
        self.grp_road.empty()
        self.grp_ground.empty()
        self.grp_border.empty()

        #ДК очищаем объекты
        self.pl = None
        self.map = None
        #Ининциализация
        self.pl = Player(pygame.Color("#ebe4e4"), 3, int((WIN_WIDTH/2) - (TILE_WIDTH/2)), WIN_HEIGHT - TILE_HEIGHT)
        self.grp_player.add(self.pl)

        self.map = GameMap(screen, level)

    def update(self):
        # Update sprites
        self.grp_player.update()
        self.grp_cars.update()
        self.grp_sand.update()
        self.grp_grass.update()
        self.grp_road.update()
        self.grp_ground.update()
        self.grp_border.update()

        # Обработка столкновений -> выстрел, астероид
        hits = pygame.sprite.groupcollide(self.sp_asteroids, self.sp_bullets, False, True)
        for hit in hits:
            hit.death()
            self.scores += 10

        # Обработка столкновений -> астероид, игрок
        hits = pygame.sprite.groupcollide(self.sp_asteroids, self.sp_player, False, False)
        for hit in hits:
            hit.death()
            self.pl.get_damage(hit.do_damage())

        # Отображение последнего прорисованного экрана.
        self.bg.update()

    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.bg.draw()
        self.sp_backgroud.draw(self.screen)
        self.sp_asteroids.draw(self.screen)
        self.sp_effects.draw(self.screen)
        self.sp_player.draw(self.screen)
        self.sp_bullets.draw(self.screen)

        self.draw_hud()
        pygame.display.flip()

    # ДК обработка событий, нажатие клавишь
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    self.pl.set_move_down()
                if event.key == K_LEFT:
                    self.pl.set_move_left()
                if event.key == K_RIGHT:
                    self.pl.set_move_right()
                if event.key == K_UP:
                    self.pl.set_move_up()

            elif event.type == pygame.KEYUP:
                if event.key == K_DOWN:
                    self.pl.unset_move_down()
                if  event.key == K_LEFT:
                    self.pl.unset_move_left()
                if  event.key == K_RIGHT:
                    self.pl.unset_move_right()
                if event.key == K_UP:
                    self.pl.unset_move_up()
