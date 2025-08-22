import os
from datetime import datetime

def get_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%d %b %Y')

def get_attributes(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            if f.is_file():
                info = f.stat()
                print(f'Modified {get_date(info.st_mtime)} {f.name}')

get_attributes('../_files')