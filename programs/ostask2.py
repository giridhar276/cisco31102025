import os
try:
    files = os.listdir("C:\\new\\new")
    for file in files:
        print(file)
except Exception as err:
    print(err)
#################################################
import os
try:
    files = os.listdir(r"C:\new\new")   # r for raw string
    for file in files:
        print(file)
except Exception as err:
    print(err)
###################################################

import os
try:
    files = os.listdir("C:/new/new")
    for file in files:
        print(file)
except Exception as err:
    print(err)