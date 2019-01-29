import os
print(__file__)

# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\tmp\path.py
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\resources\img\player.png
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1\tmp - dirname
# C:\Users\rfc_brest_m6a-719\python\ilya\platformer\lesson-15\PY-18-1 - '..'

player_image_png = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources\img', 'player.png')

print(player_image_png)