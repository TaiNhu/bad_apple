import time
from pygame import mixer

mixer.init()
mixer.music.load('bad_apple.mp3')
mixer.music.play()

with open('bad_apple.txt', 'r') as file:
    arr = file.read().split('split')
for frame in arr:
    print(frame, end='')
    time.sleep(0.01843)
