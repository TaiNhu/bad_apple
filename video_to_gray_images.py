import cv2
import os
import sys

path = r"D:/hoctap/tuhoc/python/codevovan/bad_apple/babappleimages"

video = cv2.VideoCapture('bad_apple.mp4')
index = 0
while video.isOpened():
    ret, frame = video.read()
    if ret:
        cv2.imwrite(os.path.join(path, f'bad_apple{index}.jpg'), frame)
        index += 1
        cv2.imshow('bad apple', frame)
    if cv2.waitKey(1) == ord('q'):
        sys.exit()

video.release()
cv2.destroyAllWindows()
