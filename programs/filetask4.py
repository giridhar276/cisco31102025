
# total no. of Males and females
import csv
workset = set()
mcount = 0
fcount = 0
with open("employee.csv") as fobj:
    header = fobj.readline()
    # converting file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
        gender = line[9].strip()
        if gender == "Male":
            mcount+=1
        elif gender == "Female":
            fcount+=1
    print("Total male count", mcount)
    print("Total female count:",fcount)