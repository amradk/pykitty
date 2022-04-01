import pygame
from state import State
import sys
from player import Player
from groundmap import GroundMap
from objectmap import ObjectMap
from hud import Hud
from random import randrange

from levels import all_levels
from const import *

speed_values = {
    'sand': 1,
    'grass': 2,
    'road': 3,
    'ground': 3,
}

class GameState(State):

    def __init__(self, screen, state_manager, message):
        super(State, self).__init__()
        self.state_manager = state_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.level = message['level']

    def init(self):
        self.grp_player = pygame.sprite.Group()
        self.pl = Player(pygame.Color("#ebe4e4"), 3, int((WIN_WIDTH/2) - (TILE_WIDTH/2)), WIN_HEIGHT - TILE_HEIGHT)
        self.grp_player.add(self.pl)
        self.hud = Hud(self.screen, self.pl.attempts)
        self.load_level(self.level)

    def process_message(self, message):
        if message:
            if message['level']:
                self.level = message['level']
                self.load_level(self.level)

    def load_level(self, level_num):
        self.screen.fill((0, 0, 255))
        # устанавливаем параметры игрока на начальные значения 
        self.pl.set_speed(0)
        self.pl.set_x(int((WIN_WIDTH/2) - (TILE_WIDTH/2)))
        self.pl.set_y(WIN_HEIGHT - TILE_HEIGHT)
        self.pl.attempts = 3

        self.hud.set_attempts(self.pl.attempts)

        # загружаем карту
        self.lvl_ground = GroundMap(self.screen, all_levels[1])
        self.lvl_ground.load_map()
        self.lvl_objects = ObjectMap(self.screen, all_levels[1])
        self.lvl_objects.load_map()

    def check_collision(self):
        ground_collisions = self.lvl_ground.check_collision(self.grp_player)

        # устанавливаем скорость в зависимости от типа поверхности
        speed_map = []
        for v in ground_collisions:
            speed_map.append(speed_values[v])
        if not speed_map:
            speed_map.append(3)
        self.pl.set_speed(min(speed_map))
        object_collisions = self.lvl_objects.check_collision(self.grp_player)
        if object_collisions:
            for c in object_collisions:
                if c == 'fin':
                    self.level += 1
                    self.state_manager.go_to('finlevel', 'init', {'level':self.level - 1})
                if c == 'cars':
                    self.pl.attempts -= 1
                    if self.pl.attempts <= 0:
                        self.state_manager.go_to('gameover', 'init')
                    self.pl.return_to_start()
                    self.hud.set_attempts(self.pl.attempts)

    def update(self):
        # Update sprites
        self.grp_player.update()
        if self.pl.get_x() > self.screen_rect.right - TILE_WIDTH:
            self.pl.set_x(self.screen_rect.right - TILE_WIDTH)
        if self.pl.get_x() < 0:
            self.pl.set_x(0)

        self.lvl_objects.update()
        # Обработка столкновений -> выстрел, астероид
        self.check_collision()
        self.hud.update()


    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.

        self.lvl_ground.draw()
        self.lvl_objects.draw()
        self.grp_player.draw(self.screen)
        self.hud.draw()
        pygame.display.flip()

    # ДК обработка событий, нажатие клавишь
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.pl.set_move_down()
                if event.key == pygame.K_LEFT:
                    self.pl.set_move_left()
                if event.key == pygame.K_RIGHT:
                    self.pl.set_move_right()
                if event.key == pygame.K_UP:
                    self.pl.set_move_up()
                if event.key == pygame.K_ESCAPE:
                    self.state_manager.go_to('title', 'init')

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.pl.unset_move_down()
                if  event.key == pygame.K_LEFT:
                    self.pl.unset_move_left()
                if  event.key == pygame.K_RIGHT:
                    self.pl.unset_move_right()
                if event.key == pygame.K_UP:
                    self.pl.unset_move_up()
