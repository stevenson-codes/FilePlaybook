import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)

copy_file('../_files/02_file.txt', '../_files/subfolder')
copy_folder('../_files/', '../_files/new_folder')