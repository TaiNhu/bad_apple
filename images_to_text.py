from PIL import Image
import os

path = r"D:\hoctap\tuhoc\python\codevovan\bad_apple\babappleimages"

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

for i in range(6527):
    with open('bad_apple.txt', 'a') as file:
        print('split', end='\n', file=file)
        image = Image.open(os.path.join(path, f'bad_apple{i}.jpg'))
        image = image.convert("L")
        width, height = image.size
        image = image.resize((99, int(99 * (height/width))))
        pixels = image.getdata()
        characters = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
        for num_char in range(len(characters)):
            print(characters[num_char], end='', file=file)
            if num_char % 99 == 0 and num_char > 1:
                print(file=file)
