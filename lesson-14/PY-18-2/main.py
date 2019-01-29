import pygame
from constants import * # Из файла constants импортируем всё
from player import Player

pygame.init() # Инициализация pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаем окно для отрисовки
pygame.display.set_caption(TITLE) # Устанавливает заголовок окна

# Загрузка ресурсов
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
# Игровой цикл
while running:
    # events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            ''' 
                Если (if) тип(type) события (event)
                равен (==)
                нажатию клавиши на клавиатуре (pygame.KEYDOWN)
            '''
            if event.key == pygame.K_ESCAPE:
                running = False


    # update()
    all_sprites.update()

    # draw()
    screen.fill(BACKGROUND_COLOR) # Заполняем экран цветом
    all_sprites.draw(screen)
    
    pygame.display.flip() # Отображаем нарисованое в Double buffer

pygame.quit()