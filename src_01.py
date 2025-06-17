import os
from PIL import Image
import datetime

def convert(filepath:list):
    images = [Image.open(img).convert('RGB') for img in filepath]

    # File to save the pdf (Desktop)
    save_directory = os.path.join(os.path.join(os.environ['USERPROFILE']),
                                  'Desktop')
    print(save_directory)

    # Creating the directory for the pdf
    os.makedirs(save_directory, exist_ok=True)

    # Create timestamp for the file name
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    try:
        # Define the filepath of the pdf file
        save_path = os.path.join(save_directory, f'image_{timestamp}.pdf')

        images[0].save(save_path, save_all=True, append_images=images[1:])

    except Exception as e:
        print(e)
        return False
