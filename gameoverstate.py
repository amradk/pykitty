import pygame
from const import *
from state import State
import sys

class GameOverState(State):

    def __init__(self, screen, state_manager):
        super(State, self).__init__()
        self.state_manager = state_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.set_game_over_mess = "Game Over"
        self.mess_x = WIN_WIDTH/2 - 100
        self.mess_y = WIN_HEIGHT/2
        # text frame
        self.text_surface = self.font.render(self.set_game_over_mess, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.mess_x, self.mess_y)
        # Группы для спрайтов
        self.sp = pygame.sprite.Group()

    def init(self):
        self.screen.fill((0, 0, 255))
        #ДК очищаем игры
        self.sp.empty()

    def update(self):
        # Update sprites
        self.sp.update()

    def set_game_over_mess(self, message):
        self.set_game_over_mess = message
        self.text_surface = self.font.render(self.set_game_over_mess, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.mess_x, self.mess_y)

    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.sp.draw(self.screen)
        self.screen.blit(self.text_surface, self.text_rect)
        pygame.display.flip()

    # ДК обработка событий, нажатие клавишь
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state_manager.go_to('title', 'init')
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
