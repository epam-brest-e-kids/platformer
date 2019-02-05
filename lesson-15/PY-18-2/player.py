import pygame
from constants import *
from settings import player_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Конструктор класса Sprite
        self.image = pygame.image.load(player_image).convert() # загружает картинку и конвертирует в нужный формат
        self.rect = self.image.get_rect() # Получает прямоугольник, ограничивающий картинку
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # центру прямоугольника задает координаты центра экрана
        # self.rect.x = WIDTH /2
        # self.rect.y = HEIGHT / 2
    
    def update(self):
        # self.rect.x += 5
        pass
    
    def draw(self):
        self.image.draw()
        pass