import os
from PIL import Image


def get_image(rel_path):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, rel_path)
    image = Image.open(abs_file_path)
    return image
