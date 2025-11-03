####### example1
try:
    with open("customers.txt") as fobj:
        print(fobj.read())
except Exception as err:   # Exception is the baseclass exception
    print("system err:",err)
############ example2 ######################
try:
    with open("customers.txt") as fobj:
        print(fobj.read())
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)
except (IndexError,KeyError) as err:
    print(err)
except Exception as err:
    print("system err:",err)