
import csv
workset = set()
with open("employee.csv") as fobj:
    header = fobj.readline()
    # converting file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
        workclass = line[1]
        workset.add(workclass)
    #print(workset)
    for work in workset:
        print(work)