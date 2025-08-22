import os

def list_dir(path):
    for file in os.listdir(path):
        print(file)

list_dir('../_files')