import pygame
from gameobject import GameObject

class Car(GameObject):
    def __init__(self, color, speedx, start_x, start_y, width=32, heigh=32):
        GameObject.__init__(self, speedx, 0, start_x, start_y, width, heigh)
        #self.image = pygame.image.load("assets/objects/shoots/laserGreen.png").convert_alpha()
        self.set_color(color)
        self.is_active = True
        #self.rect = self.image.get_rect()
        #self.rect.bottom = start_y
        #self.rect.centerx = start_x

    def update(self):
        if self.is_active == True:
            super().update()

    def set_inactive(self):
        self.is_active = False

    def set_active(self):
        self.is_active = True
