import zipfile

def read(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for file in lst:
            zfinf = archive.getinfo(file)
            print(f'{file} => {zfinf.file_size} bytes, {zfinf.compress_size} compressed')

read('./file.zip')