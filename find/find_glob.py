from pathlib import Path

def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)

glob_match('../_files', '*2*.t*')
glob_match('../_files/subfolder', '*_file_*.t*')