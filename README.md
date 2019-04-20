# Folder Actions
Python CLI utility that triggers actions based on changes in watched folders

This utility does not constantly watch folders. Once triggered, does its job and closes. It is up to user how to trigger. Using your operating system's functionalities, you can either schedule a periodic job, have it automatically triggered at system startup or even execute it manually if you like.

## How to use
Folder Actions requires a configuration file named 'config.json' at same path with executable. Here is an example content for config.json:
```
[
    {
        "action": "send2trash",
        "folder": "D:\\home\\tmp",
        "parameter": "st_atime",
        "days": 40
    }
]
```
Main object is an array of objects which defines the action that Folder Actions will execute.

## Configuration properties
action: Type of action that will be executed. This property is mandatory. Possible values:
* send2trash : Move files or folders to recycle bin/trash. This value requires other properties: folder, parameter, days

folder: Directory to be watched. Use two backslashes for Windows paths as backslash (\\) is a special character.

parameter: send2trash action will check some date from file metadata to decide the file is old enough. This property defines which date will be taken into consideration. Possible values:
* st_atime : Last access time
* st_mtime : Last modify time

days: Action will execute if the file is older than given number of days.

