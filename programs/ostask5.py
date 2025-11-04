

import sys
import os
try:
    for val in range(1,11):
        dirname = "dir" + str(val)   #dir1
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        else:
            print(dirname,"already exists")
except Exception as err:
    print(err)
    print(sys.exc_info())