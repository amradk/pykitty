import pygame
from gameobject import GameObject

class Car(GameObject):
    def __init__(self, color, speedx, start_x, start_y, animation_speed = 60 ):
        GameObject.__init__(self, speedx, 0, start_x, start_y, animation_speed)
        #self.image = pygame.image.load("assets/objects/shoots/laserGreen.png").convert_alpha()
        self.set_color(color)
        #self.rect = self.image.get_rect()
        #self.rect.bottom = start_y
        #self.rect.centerx = start_x

    #def update(self):
    #    self.rect.x += self.speedx
    #    # kill if it moves off the top of the screen
    #    if self.rect.top < 0:
    #        self.kill()