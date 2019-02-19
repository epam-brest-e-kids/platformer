import pygame
from constants import *
from settings import player_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Конструктор класса Sprite
        surface = pygame.image.load(player_image).convert_alpha() # загружает картинку и конвертирует в нужный формат
        scale_coefficient = PLAYER_SHIP_WIDTH / surface.get_rect().width
        self.image = pygame.transform.rotozoom(surface, 0, scale_coefficient)
        self.rect = self.image.get_rect() # Получает прямоугольник, ограничивающий картинку
        self.rect.midbottom = (WIDTH / 2, HEIGHT - 20) # центру прямоугольника задает координаты центра экрана
        self.speedx = 0
        self.accx = 5
    
    def update(self):
        self.speedx = 0
        key_state = pygame.key.get_pressed()
        if (key_state[pygame.K_LEFT]):
            self.speedx -= self.accx
        if (key_state[pygame.K_RIGHT]):
            self.speedx += self.accx
        
        self.rect.x += self.speedx
    
    # def draw(self):
    #     self.image.draw()
    #     pass