import cv2
import numpy as np
import os
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}

#INPUT--------------------------------

file = "3.jpg"

#-----------------------------------

dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(dir,"Input")
output = os.path.join(dir,"Output")
filepath = os.path.join(input, file)
outputpath = os.path.join(output,(Path(filepath).stem + "greyscaled" + Path(filepath).suffix))


if not os.path.exists(input):
    os.mkdir(input)
if not os.path.exists(output):
    os.mkdir(output)
if not os.path.exists(filepath) or file == "" or Path(file).suffix not in IMAGE_EXTENSIONS:
    print("Error: Invalid image file")
    exit()

img = cv2.imread(filepath)
h, w, c = img.shape
b, g, r = cv2.split(img)

for y in range(h):
    for x in range(w):
        brightness = (r[y][x] * 0.2126 + g[y][x] * 0.7152 + b[y][x] * 0.0722) // 1
        r[y][x] = brightness
        g[y][x] = brightness
        b[y][x] = brightness

greyimg = cv2.merge([b,g,r])
cv2.imwrite(outputpath,greyimg)