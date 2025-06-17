import os
from PIL import Image

image_files = ['image_01.png', 'image_02.JPG', 
               'image_03.jpg', 'image_04.jpg', 
               'image_05.jpg']
images = []

for img in image_files:
    images.append(Image.open(img).convert('RGB'))

output_path = 'output.pdf'

images[0].save(output_path, save_all=True,
               append_images=images[1:])