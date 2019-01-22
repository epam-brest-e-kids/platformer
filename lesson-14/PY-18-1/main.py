import pygame
from constants import *
from player import Player

# Основной код
pygame.init() # Инициализирует pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание экрана
pygame.display.set_caption(TITLE) # Установим заголовок окна
clock = pygame.time.Clock()

running = True # Определяет выполняется ли игра

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Игровой цикл
while running:
    clock.tick(FPS) # Ограничение по FPS
    # events()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # update()
    all_sprites.update()

    # draw()
    screen.fill(RED)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
