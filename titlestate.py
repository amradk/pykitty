import pygame
import thorpy
from state import State
from const import *
import sys


class TitleState(State):
    def __init__(self, screen, scene_manager):
        super(State, self).__init__()
        self.scene_manager = scene_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 24
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)

        #self.background = thorpy.Background(resources.background_image_path, elements=[self.box])

    def init(self):
        # menu
        self.quit_btn = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
        self.ng_btn = thorpy.make_button("New game", func = self.scene_manager.go_to, params = {'scene':'game', 'state':'init', 'message':{'level':1}})
        self.res_btn = thorpy.make_button("Resume", func = self.scene_manager.go_to, params = { 'scene':'game', 'state':'resume'})
        self.box = thorpy.Box.make(elements=[self.quit_btn, self.ng_btn, self.res_btn])
        self.menu = thorpy.Menu(self.box)
        for element in self.menu.get_population():
            element.surface = self.screen
        self.box.set_topleft((300, 200))

    def draw(self):
        self.box.blit()

    def update(self):
        self.box.update()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene_manager.go_to('game', 'resume')
            else:
                self.menu.react(event)  # the menu automatically integrate your elements

    def switch_state(self):
        pass
