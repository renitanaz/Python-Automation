# organizing files into disctionary in a folder based on extension

import os
from pathlib import Path

#def organize_dictionary():
for items in os.scandir("C:\\Users\\User\\OneDrive\\PythonAutomation\\11_Files_automation"):
    #if items.is_dir():
       # continue
    print(items.name)
    
#organize_dictionary()
