import pygame
from const import *
from gameobject import GameObject

class Player(GameObject):
    def __init__(self, color, speed, start_x, start_y, width=32, heigh=32):
        GameObject.__init__(self, 0, 0, start_x, start_y, width, heigh)
        #self.image = pygame.image.load("assets/objects/shoots/laserGreen.png").convert_alpha()
        self.set_color(color)
        self.attempts = 3
        self.is_active = True
        self.speed = speed
        #self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.noise_lvl = 0

    def update(self):
        # """Обновляет позицию корабля с учетом флага."""
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.center += self.speed
        #     self.set_image_righ()
        # if self.moving_left and self.rect.left > 0:
        #     self.center -= self.speed
        #     self.set_image_left()
        # # Обновление атрибута rect на основании self.center
        # self.rect.centerx = self.center
        # self.shield_restore()
        if self.is_active == True:
            super().update()

    def set_inactive(self):
        self.is_active = False

    def set_active(self):
        self.is_active = True

    def set_move_right(self):
        self.moving_right = True
        self.speedx = self.speed
        self.speedy = 0

    def set_move_left(self):
        self.moving_left = True
        self.speedx = -self.speed
        self.speedy = 0

    def set_move_up(self):
        self.moving_up = True
        self.speedy = -self.speed
        self.speedx = 0

    def set_move_down(self):
        self.moving_down = True
        self.speedy = self.speed
        self.speedx = 0

    def unset_move_right(self):
        self.moving_right = False
        self.speedx = 0

    def unset_move_left(self):
        self.moving_left = False
        self.speedx = 0

    def unset_move_up(self):
        self.moving_up = False
        self.speedy = 0

    def unset_move_down(self):
        self.moving_down = False
        self.speedy = 0

    def set_speed(self, new_speed):
        self.speed = new_speed
        if self.moving_up:
            self.speedy = -self.speed
        if self.moving_down:
            self.speedy = self.speed
        if self.moving_left:
            self.speedx = -self.speed
        if self.moving_right:
            self.speedx = self.speed

    def return_to_start(self):
        #self.set_x = self.start_x
        #self.set_y = self.start_y
        self.set_x(int((WIN_WIDTH/2) - (TILE_WIDTH/2)))
        self.set_y(WIN_HEIGHT - TILE_HEIGHT)
