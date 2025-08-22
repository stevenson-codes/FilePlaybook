import shutil

# Can be used to rename files and directories

def move_file(src, dst):
    shutil.move(src, dst)

move_file('../_files/text.txt', '../_files/subfolder/text.txt')
move_file('../_files', './xyz')
move_file('./xyz', '../_files')