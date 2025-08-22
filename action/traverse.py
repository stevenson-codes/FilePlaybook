import os

# os.walk() performs a breadth-first traversal 
# starting from the specified directory

def traverse(fld):
    for fldpath, dirs, files in os.walk(fld):
        print(f'Folder:  {fldpath}')
        for file in files:
            print(f'\t{file}')

traverse('../_files')