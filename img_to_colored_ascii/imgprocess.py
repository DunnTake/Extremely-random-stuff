import cv2
import numpy as np
import os
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path

#ASCII FONTS ---------------------
full = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|1{}[]?-_+~<>i!lI;:,^`'. "
classic = "@#W$9876543210?!abc;:+=-,._ "
minimal = "@%#*+=-:. "
blocky = "█▓▒░ "
#---------------------------------

#CHANGE STUFF HERE ------------------------

#PIXELATED SIZE (px)
block_size = 8

#ASCII
asci = True
afont = full

#FILE
file = "example.png" #Change this to desired file
#---------------------------------------------

folder = os.path.dirname(os.path.realpath(__file__))
input = os.path.join(folder,"Input")
output = os.path.join(folder,"Output")
address = os.path.join(input,file)
img = cv2.imread(address)
path = Path(address)
name = path.stem
imgtype = path.suffix

h, w, c = img.shape
canvas = Image.new("RGB", (w,h), color="black")
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype(r"C:\Windows\Fonts\Consola.ttf",block_size)
a = -1
b = 7

oname = str(name + (("ASCII" + ("full" if afont == full else "classic" if afont == classic else "minimal" if afont == minimal else "blocky" if afont == blocky else afont)) if asci == True else "pixilated") + str(block_size) + "px")
ofile = str(oname + imgtype)
oaddress = os.path.join(output,ofile)
#KERNEL FILTER --------------------------

kernel = np.array([
    [0,a,0],
    [a,b,a],
    [0,a,0]
])

kfilter = cv2.filter2D(img, -1, kernel)

#----------------MAIN LOGIC--------------------

h, w, c = img.shape
modimg = img

output = np.zeros_like(img)


if asci == False:
    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            patch = modimg[i:i + block_size , j:j + block_size]
            avgcolor = np.mean(patch,axis=(0,1))

            output[i:i + block_size, j:j + block_size] = avgcolor # B, G, R
    
    cv2.imshow("pixil",output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            patch = modimg[i:i + block_size , j:j + block_size]
            avgcolor = tuple(np.mean(patch,axis=(0,1)).astype(int))
            alen = 255/len(afont)
            bright = avgcolor[0]*0.0593 + avgcolor[1]*0.678 + avgcolor[2]*0.2627
            if bright == 255:
                char = len(afont) - 1
            else:
                char = bright//alen
            achar = int(len(afont) - 1 - char)
            draw.text((j,i), afont[achar], font=font, fill = (avgcolor[2],avgcolor[1],avgcolor[0]))

    canvas.show()
    canvas.save(oaddress)
