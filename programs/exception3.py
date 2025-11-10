


try :
    fobj = open("customers.txt")
except Exception as err:
    print(err)
else:
    for line in fobj:
        print(line)
    fobj.close()
finally:
    print("end of file handling")
