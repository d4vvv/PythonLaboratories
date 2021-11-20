import os

def list_files():
    path = "C:/Users/Kacper/Desktop/AGH/WTAS" #example path
    totalFiles = 0

    for base, dirs, files in os.walk(path):
        for Files in files:
            totalFiles += 1

    print(totalFiles)

list_files()