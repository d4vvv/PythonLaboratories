import os

def list_files():
    path = "C:/Users/Kacper/Desktop/AGH/WTAS" #example path

    for base, dirs, files in os.walk(path):
        for Files in files:
            print(base + " " + Files)


list_files()