import pygame
import os
from settings import *
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'player.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    def update(self):
        # self.rect.x += 5
        pass