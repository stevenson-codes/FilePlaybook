import os, fnmatch

def match(path, search):
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, search):
            print(file)

match('../_files', '*_file*.*')
match('../_files', '*_file_*.*')
match('../_files', '*2_*_*.*')