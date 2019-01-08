import pygame # Импортируем библиотеку pygame
import sys
from settings import * # Импортируем всё из модуля settings
from levels.menu import Menu
from levels.level1 import Level1

# Определение основного класса игры
class Game:
  # Это наш конструктор
  def __init__(self):
      pygame.init() # Инициализация движка pygame
      pygame.mixer.init() # Инициализация миксера для звуков
      pygame.font.init()
      self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание экрана игры
      pygame.display.set_caption(TITLE) # Установка заголовка для игры
      self.clock = pygame.time.Clock() # Создание "часов" для контроля FPS

      self.playing = False
      self.paused = False
  
  def start(self):
    self.playing = True # Пока self.playing == True игра выполняется
    self.load_level(MENU)
    
    # Это основной game loop игры
    while self.playing: # Бесконечный игровой цикл
      self.clock.tick(FPS) # Ограничиваем отрисовку с заданым FPS
      self.events() # Обрабатываем события игры
      if not self.paused:
        self.update() # Обрабатываем физику и все действия в игре
      self.draw() # Отображаем что получилось
  
  # Эта функция вызывается, когда мы хотим выйти из игры
  def quit(self):
    pygame.quit() # Эта функция вызывает выход из pygame
    sys.exit() # Закрываем окно

  ##################### Секция для загрузки менюшек ##################
  
  # Отображаем уровень или меню игры
  def load_level(self, level):
    if (level == LEVEL1):
      self.level = Level1()
    else:
      self.level = Menu()

  
  ###################### Game Loop - Игровой цикл ####################
  
  # Обработка событий в самой игре
  def events(self):
    for event in pygame.event.get(): # Для каждого события из всех событий в pygame
      if event.type == pygame.QUIT: # Если произошло событие выход
        self.quit() # Вызываем метод выхода из игры
      if event.type == pygame.KEYDOWN: # Если нажата клавиша на клавиатуре
        if event.key == pygame.K_ESCAPE: # Если нажат Escape
            self.quit() # Выйдем из игры
        if event.key == pygame.K_p: # Если нажата клавиша p
            self.paused = not self.paused # Ставим игру на паузу

  def update(self):
    self.level.update()

  def draw(self):
    self.level.draw()
    pygame.display.flip()


# Создаём экземпляр класса игры
g = Game() # Тут вызовется конструктор класса

try:
  g.start() # Запустим игру
except SystemExit:
  pass