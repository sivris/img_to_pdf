import os
from PIL import Image

A4_x = 2480
A4_y = 3508

img = Image.new(mode='RGB', size=(2480, 3508), color='White')
img2 = Image.open('lisence1.jpg')
img2 = img2.rotate(angle=270, fillcolor='white')
img2.thumbnail((1500, 2300))


img.paste(img2)

img.save('white.pdf', resolution=300.0)
