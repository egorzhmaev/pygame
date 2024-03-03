import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        # Инициализирует корабль и задает его начальную позицию
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получения прямоугольника
        self.image = pygame.image.load('venv/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Сохранение вещественной координаты центра коробля
        self.center = float(self.rect.centerx)
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
    def update(self):
        # Обновляет позицию коробля
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Обновление атрибута rect
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx