##write a progarm to display all the files only  from C: line by line 
import os
try:
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            print(file)
except Exception as err:
    print(err)
######################### display directories only
import os
try:
    files = os.listdir()
    for file in files:
        if os.path.isdir(file):
            print(file)
except Exception as err:
    print(err)