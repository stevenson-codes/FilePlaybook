import os

def remove_file(file):
    if os.path.isfile(file):
        try:
            os.remove(file)
        except OSError as e:
            print(f'Error: {f} : {e.strerror}')
    else:
        print(f'Error: {file} is not a valid file')

remove_file('../_files/text.txt')