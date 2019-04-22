# Folder Actions
Python CLI utility that triggers actions based on changes in watched folders

This utility does not constantly watch folders. Once triggered, does its job and closes. It is up to user how to trigger. Using your operating system's functionalities, you can either schedule a periodic job, have it automatically triggered at system startup or even execute it manually if you like.

## Download
[Latest release binary](https://github.com/kkayacan/folder-actions/releases/latest/download/folder-actions.zip)

## How to use
Folder Actions requires a configuration file named 'config.json' at same path with executable. Here is an example content for config.json:
```
[
    {
        "action": "send2trash",
        "folder": "D:\\home\\tmp",
        "parameter": "st_atime",
        "days": 40
    },
    {
        "action": "copy",
        "source": "D:\\home\\cloud\\OneDrive\\Appdata",
        "destination": "D:\\home\\cloud\\Google\\Appdata",
        "days": 2
    },
    {
        "action": "popen",
        "folder": "D:\\home\\cloud\\Google\\Appdata",
        "command": "C:\\Program Files\\Google\\Drive\\googledrivesync.exe",
        "days": 2
    }
]
```
Main object is an array of objects which defines the action that Folder Actions will execute.

## Configuration
### send2trash
Move old files or folders to recycle bin/trash. Properties:

**action**: "send2trash"

**folder**: Directory to be watched. Use two backslashes for Windows paths as backslash (\\) is a special character.

**parameter**: send2trash action will check some date from file metadata to decide if the file is old enough. This property defines which date will be taken into consideration. Possible values:
* st_atime : Last access time
* st_mtime : Last modify time

**days**: Action will execute if the file is older than given number of days.


### copy
Copy recently changed files to another destination. Existing files with same name in destination will be overwrited. Properties:

**action**: "copy"

**source**: Folder to be watched

**destination**: Path to folder which the files will be copied at

**days**: Action will execute if the file is modified not before given number of days

### popen
Start a system process if files in a folder changed recently. Properties:

**action**: "popen"

**folder**: Directory to be watched. Use two backslashes for Windows paths as backslash (\\) is a special character.

**command**: Process path to be started

**days**: Action will execute if the file is modified not before given number of days

## Future plans
* Execution log
* GUI for configuration
* File filters
* Complex conditions
* Dependent/multiple actions for a condition