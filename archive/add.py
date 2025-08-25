import zipfile

to_add = [
    './add.py'
]

def add(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for file in files:
            lst = archive.namelist()
            if file not in lst:
                archive.write(file)
            else:
                print(f'File exists')

add('./file.zip', to_add, 'a')