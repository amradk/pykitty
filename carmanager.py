import pygame
import random
from car import Cart

class CarManager():
    def __init__(self, start_x, start_y, max_cars):
        self.start_x = start_x
        self.start_y = start_y
        self.max_cars = max_cars
        self.grp_car = pygame.sprite.Group()

    def update(self):
        self.grp_car.update()

    def create_cars(self):
        for i in xrange(max_cars):
            color = list(random.choice(range(256), size=3))
            c = Car(color, random.randint(1, 5), self.start_x, self.start_y)
            self.grp_car.add(c)
