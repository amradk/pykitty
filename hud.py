import pygame
from const import *
from gameobject import GameObject

class Hud():
    def __init__(self, screen, attempts):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        (self.screen_width, self.screen_height) = self.screen.get_size()
        self.num_of_attempts = attempts
        self.attempts_sprite_list = []

        self.attempts = pygame.sprite.Group()
        #for i in player.get_attempts():
        x = 10
        for i in range(self.num_of_attempts):
            attempt = GameObject(x=x, y=10, width=16, heigh=16)
            self.attempts_sprite_list.append(attempt)
            attempt.set_color(RED)
            x += 32
            self.attempts.add(attempt)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, WHITE)
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

    def set_attempts(self, attempts):
        print("Attempt=",len(self.attempts_sprite_list))
        # кол-во попыток усеньшилось
        if (self.num_of_attempts - attempts) > 0:
            self.attempts.remove(self.attempts_sprite_list[-1])
            del self.attempts_sprite_list[-1]
        self.num_of_attempts = attempts
