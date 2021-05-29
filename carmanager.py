import pygame
import random
#import sys
from car import Car

class CarManager():
    def __init__(self, screen, start_x, start_y, speed, direction, max_cars):
        self.start_x = start_x
        self.start_y = start_y
        self.max_cars = max_cars
        self.direction = direction
        self.speed = self.direction * speed
        self.gap = 96
        self.grp_car = pygame.sprite.Group()
        self.screen = screen
        (self.screen_width, self.screen_height) = self.screen.get_size()

    def update(self):
        for c in self.grp_car:
            if self.direction > 0:
                if c.get_x() > self.screen_width:
                    c.set_x(self.start_x)
            if self.direction < 0 :
                if c.get_x() < 0:
                    c.set_x(self.start_x)
        self.grp_car.update()

    def draw(self):
        self.grp_car.draw(self.screen)

    def set_diretcion(self, direction):
        pass

    def create_cars(self):
        x = self.start_x
        for i in range(self.max_cars):
            color = list(random.choices(range(256), k=3))
            c = Car(color, self.speed, x, self.start_y)
            self.grp_car.add(c)
            x = x + self.gap

