import pygame
from gameobject import GameObject

class Hud():
    def __init__(self, screen, player):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        (self.screen_width, self.screen_height) = self.screen.get_size()
        # define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.BAR_LENGTH = 100
        self.BAR_HEIGHT = 10
        #
        self.attempts = pygame.sprite.Group()
        #for i in player.get_attempts():
        x = 10
        for i in range(3):
            attempt = GameObject(x=x, y=10, width=16, heigh=16)
            attempt.set_color(self.RED)
            x += 32
            self.attempts.add(attempt)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_attempts(self, player):
        self.attempts.draw(self.screen)

    def draw_hud(self):
        self.draw_health_bar()
        self.draw_shield_bar()
        self.draw_text(str(self.scores), self.score_x, self.score_y)

    def update(self):
        pass

    def draw(self):
        self.attempts.draw(self.screen)
