# organizing files into disctionary in a folder based on extension

import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDictionary(value):
    for category , suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

def organize_dictionary():
    for items in os.scandir("C:\\Users\\User\\OneDrive\\PythonAutomation\\Files_automation\\Exercise Files\\OrganizeMe"):
        if items.is_dir():
            continue
        #print(items)
        filePath = Path(items)
        filetype = filePath.suffix.lower()
        directory = pickDictionary(filetype)
        #print(directory)
        directoryPath = Path("C:\\Users\\User\\OneDrive\\PythonAutomation\\Files_automation\\Exercise Files\\OrganizeMe" ,directory)
        if directoryPath.is_dir() !=True:
            directoryPath.mkdir()
        #print ("directoryPath",directoryPath)
        #print("filePath",filePath)    
        #print(items.name)
        #print("join path",directoryPath.joinpath(items.name))
        os.rename(filePath,directoryPath.joinpath(items.name))

organize_dictionary()
