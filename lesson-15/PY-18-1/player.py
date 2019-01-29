import pygame
import os
from settings import player_image
from constants import *
print(__file__) 
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\player.py

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(player_image).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    def update(self):
        # self.rect.x += 5
        pass