import os

# __file__ ==
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-2\settings.py
game_folder = os.path.dirname(__file__) # Папка с игрой
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-2

resource_folder = os.path.join(game_folder, 'resources')
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-2\resources

image_folder = os.path.join(resource_folder, 'img')
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-2\resources\img

player_image = os.path.join(image_folder, 'player.png')

# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-2\resources\img\player.png

# player_image = os.path.join(game_folder, 'resources', 'img', 'player.png')