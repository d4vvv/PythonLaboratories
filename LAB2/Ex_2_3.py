import os
from PIL import Image

def convert_jpg_to_png():
    path = "C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB2"

    for base, dirs, files in os.walk(path):
        for File in files:
            im = Image.open(base + "/" + File)
            im.save(base + "/" + File.replace("jpg", "png"))
            print(File + " " + File.replace("jpg", "png"))

convert_jpg_to_png()