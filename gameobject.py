import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, group, speedx = 0, speedy = 0, x = 0, y = 0, width=32, heigh=32):
        pygame.Surface.__init__(self, (width, heigh))
        """Инициализирует корабль и задает его начальную позицию."""
        self.group = group
        self.image = pygame.Surface((32, 32))
        self.speedx = speedx
        self.speedy = speedy
        self.rect = self.image.get_rect()
        # Устанавливаем начальные координаты
        self.start_y = y
        self.start_x = x
        self.color = '#000000'

    def set_color(self, color):
        self.image.fill(Color(self.color))

    def update(self):
        self.rect.top += self.speedy
        self.rect.centerx += self.speedx

    def set_speed_x(self, speed_x):
        self.speedx = speed_x

    def set_speed_y(self, speed_y):
        self.speedy = speed_y

    def get_x(self):
        return self.rect.left

    def get_y(self):
        return self.rect.top

    def get_height(self):
        return self.rect.height

    def get_widht(self):
        return self.rect.width

    def set_y(self, y):
        self.rect.top = y

    def set_x(self, x):
        self.rect.centerx = x