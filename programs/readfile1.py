# method1: reading the file line by line
with open("customers.txt") as fobj:
    for line in fobj:
        print(line.strip())

# method2: reading using fobj.read()-----> wil return the string 
# not suggestable for larger files
# just like Ctrl + A     Ctrl + C    Ctrl + V
with open("customers.txt","r") as fobj:
    print(fobj.read())

# method3:  using fobj.readlines()  ------> list
with open("customers.txt","r") as fobj:
    # will return the list
    print(fobj.readlines())

# method4 : using csv library
import csv   # builtin library
with open("customers.txt","r") as fobj:
    # converting file object to csv object
    reader = csv.reader(fobj)
    # each line will be converted to list automatically
    for line in reader:
        print(line)


# method5 : using pandas 
import pandas as pd 
df = pd.read_csv("customers.txt")
print(df)


#pip install pandas  ( windows)
#pip3 install pandas ( Mac)

    