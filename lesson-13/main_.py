import pygame
from constants import *

# Основной код
pygame.init() # Инициализирует pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание экрана
pygame.display.set_caption(TITLE) # Установим заголовок окна
clock = pygame.time.Clock()

running = True # Определяет выполняется ли игра

# Игровой цикл
while running:
    clock.tick(FPS) # Ограничение по FPS
    # events()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # update()
    pass

    # draw()
    screen.fill(RED)
    pygame.display.flip()

pygame.quit()
