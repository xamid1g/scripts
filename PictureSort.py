import os
import shutil

#script to move files in an unsorted dir to the right folders

#variables that need to be changed!!!
#date is the starttag of the pictures
date = "202010"

#month of the year
month = "10"

#directory of raw files
rawFilesPath = 'D:/OneDrive/Bilder/Eigene Aufnahmen/2020/'

#creating new dir
new_dir = os.path.join(rawFilesPath,month)
#checks if dir already exists
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

#list files in path dir
files = os.listdir(rawFilesPath)

for file in files:
    #checks the chars at the start of every file
    if file.startswith(date):
        #rename files to new dir
        os.rename(rawFilesPath + os.path.basename(file),rawFilesPath + month + "/" + os.path.basename(file))