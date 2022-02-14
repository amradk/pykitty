import pygame
import random
#import sys
from car import Car

class CarManager():
    def __init__(self, screen, start_x, start_y, speed, direction, max_cars):
        self.car_sizes = [32, 64, 96]
        self.gap_sizes = [64, 96, 126]
        self.start_x = start_x
        self.start_y = start_y
        self.max_cars = max_cars
        self.direction = direction
        self.speed = self.direction * speed
        self.grp_car = pygame.sprite.Group()
        self.screen = screen
        self.active_cars = max_cars
        (self.screen_width, self.screen_height) = self.screen.get_size()

    def choose_speed(self):
        self.speed = random.randrange(1,6) * self.direction


    def update(self):
        if self.active_cars <= 0:
            x = self.start_x
            self.choose_speed()
            for c in self.grp_car:
                gap = random.choice(self.gap_sizes)
                c.set_active()
                c.set_speed_x(self.speed)
                self.active_cars = self.active_cars + 1
                c.set_x(x)
                x = x + c.image.get_width() + gap

        else:
            for c in self.grp_car:
                if self.direction > 0:
                    if c.get_x() > 1024:
                        c.set_inactive()
                        self.active_cars = self.active_cars - 1
                if self.direction < 0:
                    if c.is_active == True:
                        if c.get_x() < (0 - c.image.get_width()):
                            #c.set_x(self.start_x)
                            c.set_inactive()
                            self.active_cars -= 1

        self.grp_car.update()

    def draw(self):
        self.grp_car.draw(self.screen)

    def set_diretcion(self, direction):
        pass

    def create_cars(self):
        x = self.start_x
        for i in range(self.max_cars):
            color = list(random.choices(range(256), k=3))
            car_size = random.choice(self.car_sizes)
            gap = random.choice(self.gap_sizes)
            self.grp_car.add(Car(color, self.speed, x, self.start_y, car_size, 32))
            x = x + car_size + gap
