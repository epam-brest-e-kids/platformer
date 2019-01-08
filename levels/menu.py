import pygame
from .base_level import BaseLevel
from settings import *

from random import randint

class Menu(BaseLevel):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("fonts/Creepster-Regular.ttf", 105)
        self.background_color = BLACK
        self.step = 5
        self.sign = [1,1,1]

    def update_color(self, index):
        color = self.background_color[index] + self.sign[index] * randint(0, self.step)

        if (color > 255):
            color = 255
            self.sign[index] = - self.sign[index]
        if (color < 0):
            color = 0
            self.sign[index] = - self.sign[index]
        
        return color
    
    def new_background(self):
        red = self.update_color(0)
        green = self.update_color(1)
        blue = self.update_color(2)
        self.background_color = (red, green, blue)

    def update(self):
        self.new_background()
    
    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(self.background_color)
        text_surface = self.font.render("PLATFORMER", True, RED)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text_surface, text_rect)
    
    def unload(self):
        self.font = None
