import pygame
from gameobject import GameObject

class Player(GameObject):
    def __init__(self, color, speed, start_x, start_y, width=32, heigh=32):
        GameObject.__init__(self, 0, 0, start_x, start_y, width, heigh)
        #self.image = pygame.image.load("assets/objects/shoots/laserGreen.png").convert_alpha()
        self.set_color(color)
        self.is_active = True
        self.speed = speed
        #self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.is_active == True:
            super().update()

    def set_inactive(self):
        self.is_active = False

    def set_active(self):
        self.is_active = True

    def set_move_right(self):
        print("Move right")
        print("Pl X is:", self.rect.left)
        print("Pl Y is:", self.rect.top)
        self.moving_right = True
        self.speedx = self.speed
        self.speedy = 0

    def set_move_left(self):
        print("Move left")
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
