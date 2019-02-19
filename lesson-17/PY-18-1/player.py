import pygame
import os
from settings import player_image
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        raw_surface = pygame.image.load(player_image).convert_alpha()
        scale_coefficient = PLAYER_SHIP_WIDTH / raw_surface.get_rect().width
        self.image = pygame.transform.rotozoom(\
            raw_surface,\
            0,\
            scale_coefficient\
        )
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT - 20)
        self.speedx = 0
    
    def update(self):
        self.speedx = 0
        key_state = pygame.key.get_pressed()
        if (key_state[pygame.K_a]):
            self.speedx = -5
        if (key_state[pygame.K_d]):
            self.speedx = 5
        self.rect.x += self.speedx
