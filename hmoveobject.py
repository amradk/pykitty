# horizontaly moved object
import pygame
import const

from gameobject import GameObject

class HMoveObject(GameObject):
    def __init__(self, color, speedx, start_x, start_y, width=32, heigh=32):
        GameObject.__init__(self, speedx, 0, start_x, start_y, width, heigh)
        #self.image = pygame.image.load("assets/objects/shoots/laserGreen.png").convert_alpha()
        self.set_color(color)
        self.is_active = True

    def update(self):
        if self.is_active == True:
            super().update()
        if self.behaviour:
            if self.behaviour['move_mode'] == 'patrol':
                if self.speedx > 0:
                    if self.rect.left > (self.start_x + self.rect.width * self.behaviour['move_radius']):
                        self.speedx = -self.speedx
                if self.speedx < 0:
                    if self.rect.left < (self.start_x - self.rect.width * self.behaviour['move_radius']):
                        self.speedx = -self.speedx
            if self.behaviour['move_mode'] == 'move_fwd':
                if self.get_x() > const.WIN_WIDTH:
                    self.rect.left = self.start_x

    def set_inactive(self):
        self.is_active = False

    def set_active(self):
        self.is_active = True

    def set_behaviour(self, behaviour):
        # { 
        #     'move_mode' : 'patrol', # move_fwd
        #     'move_radius' : 3,
        #     'move_direction' : 'direct' # reverse
        # }
        self.behaviour = behaviour
        if self.behaviour['move_direction'] == 'reverse':
            self.speedx = -self.speedx
