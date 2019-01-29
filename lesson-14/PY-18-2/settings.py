import os

game_folder = os.path.dirname(__file__) # Папка с игрой
resource_folder = os.path.join(game_folder, 'resources')
image_folder = os.path.join(resource_folder, 'img')
path_to_player = os.path.join(image_folder, 'player.png')