import zipfile

to_zip = [
    './zip.py',
]

def zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for file in files:
            archive.write(file)

zip('./file.zip', to_zip, 'w')