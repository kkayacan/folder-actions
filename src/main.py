from datetime import datetime
from os import scandir
from send2trash import send2trash

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d.%m.%Y %H:%M:%S')
    return formated_date

def get_files():
    dir_entries = scandir('D:\\home\\tmp')
    for entry in dir_entries:
        info = entry.stat()
        print(f'{entry.path}')
        print(f'Last Modified: {convert_date(info.st_mtime)}')
        print(f'Last Accessed: {convert_date(info.st_atime)}')
        delta = (datetime.utcnow() - datetime.utcfromtimestamp(info.st_atime)).days
        print(f'Days passed: {delta}')
        if delta > 35:
            send2trash(entry.path)
            print(f'DELETE')
        print(f'')

get_files()