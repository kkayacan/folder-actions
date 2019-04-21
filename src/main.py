import os
import sys
import shutil
import json
from datetime import datetime
from send2trash import send2trash


def get_config():
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as f:
        datastore = json.load(f)
        return datastore


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d.%m.%Y %H:%M:%S')
    return formated_date


def remove(path, parameter, days):
    dir_entries = os.scandir(path)
    for entry in dir_entries:
        info = entry.stat()
        # print(f'{entry.path}')
        #print(f'Last Modified: {convert_date(info.st_mtime)}')
        #print(f'Last Accessed: {convert_date(info.st_atime)}')
        if parameter == "st_atime":
            key_time = info.st_atime
        elif parameter == "st_mtime":
            key_time = info.st_mtime
        delta = (datetime.utcnow() - datetime.utcfromtimestamp(key_time)).days
        #print(f'Days passed: {delta}')
        if delta > days:
            send2trash(entry.path)
            # print(f'DELETE')


def copy(source, destination, days):
    dir_entries = os.scandir(source)
    for entry in dir_entries:
        info = entry.stat()
        delta = (datetime.utcnow() -
                 datetime.utcfromtimestamp(info.st_mtime)).days
        if delta <= days:
            try:
                shutil.copy(entry.path, destination)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())

config = get_config()
for action in config:
    if action["action"] == "send2trash":
        remove(action["folder"], action["parameter"], action["days"])
    elif action["action"] == "copy":
        copy(action["source"], action["destination"], action["days"])
