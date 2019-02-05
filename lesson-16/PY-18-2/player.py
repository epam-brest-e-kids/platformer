import pygame
from constants import *
from settings import player_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Конструктор класса Sprite
        # Х1=193 Y1=0 X2=708 Y2=401
        surface = pygame.image.load(player_image).convert() # загружает картинку и конвертирует в нужный формат
        self.image = pygame.transform.scale(surface, (50, 50))
        self.rect = self.image.get_rect() # Получает прямоугольник, ограничивающий картинку
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # центру прямоугольника задает координаты центра экрана
    
    # def update(self):
    #     # self.rect.x += 5
    #     pass
    
    # def draw(self):
    #     self.image.draw()
    #     pass