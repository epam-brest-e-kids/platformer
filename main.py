import pygame # Импортируем библиотеку pygame
from settings import * # Импортируем из файла settings.py всё содержимое

class Game(object):
  # Конструктор класса
  def __init__(self):
    pygame.init() # Инициализация(настройка) pygame для работы
    self.scene = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание окна в котором рисуем
    pygame.display.set_caption(TITLE) # Установка заголовка для окна
    self.clock = pygame.time.Clock()
    self.playing = False # Создаем атрибут класса Game "playing"
  
  # Запускает игру в бесконечном цикле
  def run(self):
    self.playing = True # Установим атрибут playing, показывая что игра началась
    while self.playing: # Пока атрибут playing равен True будет выполняться этот цикл
      self.clock.tick(FPS)
      self.draw() # Запускает отрисовку
  
  # Отрисовывает то, что было прорисовано
  def draw(self):
    self.scene.fill(RED)
    pygame.display.flip() # Отображает в окне то, что было нарисовано


g = Game() # Создаем экземпляр игры
g.run() # Выполняем метод run, чтобы запустить игру
