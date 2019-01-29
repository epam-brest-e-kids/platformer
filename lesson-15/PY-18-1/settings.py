import os 

game_folder = os.path.dirname(__file__) # Папка с игрой
resource_folder = os.path.join(game_folder, 'resources') # Папка ресурсов
img_folder = os.path.join(resource_folder, 'img') # Папка картинок
# __file__ == 'C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\settings.py'
# game_folder == 'C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1'
# resource_folder == 'C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\resources'
# player_image == 'C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\resources\img\player.png'
player_image = os.path.join(img_folder, 'player.png')
