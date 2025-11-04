
#write a program to display all the files and directories from current directory line by line
import os
try:
    files = os.listdir()
    for file in files:
        print(file)
except Exception as err:
    print(err)
################################################
import glob 
try:
    files = glob.glob("*.*")
    for file in files:
        print(file)
except Exception as err:
    print(err)
