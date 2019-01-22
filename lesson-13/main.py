import pygame

# Определение констант
WIDTH = 640 # Ширина окна
HEIGHT = 480 # Высота окна
FPS = 60 # Кадры в секунду
TITLE = "Platformer"

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (64, 177, 247)

pygame.init() # Инициализация pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаем окно для отрисовки
pygame.display.set_caption(TITLE) # Устанавливает заголовок окна

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
    pass

    # draw()
    screen.fill(BACKGROUND_COLOR) # Заполняем экран цветом
    
    pygame.display.flip() # Отображаем нарисованое в Double buffer

pygame.quit()