import os

def ends_with(path, search):
    for file in os.listdir(path):
        if file.endswith(search):
            print(file)

def starts_with(path, search):
    for file in os.listdir(path):
        if file.startswith(search):
            print(file)

ends_with('../_files', '.txt')
starts_with('../_files', '01_test')