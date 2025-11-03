

with open("employee.csv") as fobj:
    # just reading first line
    header = fobj.readline().split(",")
    print("Total no. of columns :",len(header))
    print("Total no. of rows    :", len(fobj.readlines()))
