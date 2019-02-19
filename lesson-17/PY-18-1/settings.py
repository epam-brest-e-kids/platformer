import os 

game_folder = os.path.dirname(__file__) # Папка с игрой
resource_folder = os.path.join(game_folder, 'resources') # Папка ресурсов
img_folder = os.path.join(resource_folder, 'img') # Папка картинок
player_image = os.path.join(img_folder, 'player.png') # Картинка игрока
