import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, speedx = 0, speedy = 0, x = 0, y = 0, width=32, heigh=32):
        pygame.sprite.Sprite.__init__(self)
        """Инициализирует корабль и задает его начальную позицию."""
        self.image = pygame.Surface((width, heigh))
        self.speedx = speedx
        self.speedy = speedy
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        # Устанавливаем начальные координаты
        self.start_y = y
        self.start_x = x
        self.color = '#000000'
        self.add(self.group)

    def set_color(self, color):
        self.color = color
        self.image.fill(pygame.Color(color))

    def update(self):
        self.rect.top += self.speedy
        self.rect.centerx += self.speedx

    def draw(self):
        self.image.fill(pygame.Color(self.color))

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