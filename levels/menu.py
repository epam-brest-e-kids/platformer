import pygame
from .base_level import BaseLevel
from settings import *

class Menu(BaseLevel):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("fonts/Creepster-Regular.ttf", 105)
    
    def draw(self):
        screen = pygame.display.get_surface()
        text_surface = self.font.render("PLATFORMER", True, RED)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text_surface, text_rect)
    
    def unload(self):
        self.font = None
