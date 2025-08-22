import os
from pathlib import Path

def rename_file(src, dst):
    os.rename(src, dst)

def rename_file2(src, dst):
    f = Path(src)
    f.rename(dst)

# rename_file('../_files/text.txt', '../_files/test.txt')
rename_file('../_files/test.txt', '../_files/text.txt')
