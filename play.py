import time
from playsound import playsound
import threading
import sys

f = threading.Thread(target=lambda: playsound('bad_apple.mp3'))
f.start()

with open('bad_apple.txt', 'r') as file:
    arr = file.read().split('split')
for frame in arr:
    print(frame, end='')
    #time.sleep(0.029)
print("\nTurn off terminal to exit\nthis is error i don't know how to kill multithread")
