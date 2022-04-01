import pygame
from const import *
from state import State
import sys

class LevelFinishState(State):

    def __init__(self, screen, state_manager, mess):
        super(State, self).__init__()
        self.state_manager = state_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.mess_x = WIN_WIDTH/2 - 100
        self.mess_y = WIN_HEIGHT/2
        # Группы для спрайтов
        self.sp = pygame.sprite.Group()
        self.level = mess['level']
        self.lvl_fin_mess = "Level " + str(self.level) + " Complete"

    def init(self):
        self.screen.fill((0, 0, 255))
        #ДК очищаем игры
        # text frame
        self.text_surface = self.font.render(self.lvl_fin_mess, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.mess_x, self.mess_y)
        self.sp.empty()

    def process_mess(self, message):
        print("Mess=",message)
        if message:
            if message['level']:
                self.level = message['level']
                self.set_message('Level ' + str(self.level) + ' complete!')


    def update(self):
        # Update sprites
        self.sp.update()

    def set_message(self, message):
        self.message = message
        self.text_surface = self.font.render(self.message, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.mess_x, self.mess_y)

    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.sp.draw(self.screen)
        self.screen.blit(self.text_surface, self.text_rect)
        pygame.display.flip()

    # ДК обрm аботка событий, нажатие клавишь
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state_manager.go_to('game', 'resume', {'level':self.level + 1})
                elif event.key == pygame.K_ESCAPE:
                    self.state_manager.go_to('game', 'resume', {'level':self.level + 1})
