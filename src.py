# Python3 program to convert image to pdf
# using img2pdf library

# importing necessary libraries
import datetime
import img2pdf
from PIL import Image
import os

def convert(path:str, cnt:int):
    # File to save the pdf (Desktop)
    save_directory = os.path.join(os.path.join(os.environ['USERPROFILE']),
                                  'Desktop')
    print(save_directory)

    # Creating the directory for the pdf
    os.makedirs(save_directory, exist_ok=True)

    # Create timestamp for the file name
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # Define the filepath of the pdf file
    save_path = os.path.join(save_directory, f'image_{timestamp}+{cnt}.pdf')
    print(save_path)

    # storing image path
    img_path = path
    
    try:
        # opening image
        image = Image.open(img_path)
        
        # converting into chunks using img2pdf
        pdf_bytes = img2pdf.convert(image.filename)
        
        # opening or creating pdf file
        file = open(save_path, "wb")
        print(file)
        
        # writing pdf files with chunks
        file.write(pdf_bytes)
        
        # closing image file
        image.close()
        
        # closing pdf file
        file.close()

        return True
    
    except Exception as e:
        print(e)
        return False
