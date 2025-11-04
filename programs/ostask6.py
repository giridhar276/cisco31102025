import datetime
import os
import time
import calendar
print(os.getcwd())
print(os.getlogin())
#print(os.environ)  ### display all enviornment variables
for key,value in os.environ.items():
    print(key,value)
### display the current timestamp
print(datetime.datetime.now())
print(time.ctime())
print(calendar.calendar(2026))
print(calendar.month(2025,10))
# epoch time - 1762232468.0319774
epoch = os.path.getatime("employee.csv")
print(datetime.datetime.fromtimestamp(epoch))
print(os.getpid())
print(os.getppid())