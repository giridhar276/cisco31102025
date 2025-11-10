
######### fixed arguments #############
def display(a,b):
    c = a + b
    return c

total = display(10,20)
print(total)

####### default arguments #############
def display(a = 0,b = 0,c = 0 ,d = 0):
    print(a,b,c,d)

display()
display(10)
display(10,20)
display(10,20,30)
display(10,20,30,40)


########## keyword arguments ##############
def display(c,a,b):
    print(a,b,c)

display(b = 20,a=10,c = 30)

########## variable length arguments ############

# in python if any object begins with * ... it is treated as tuple
def display(*data):
    print(data)
    for value in data:
        print(value)

display(10,20,30,40,50,60,70,80,90,100,12,13,24,43,56,54,54,655,4,90,56,43,43,543,43)

def displayinfo(**kwargs):  # kwargs is a dictionary
    for key,value in kwargs.items():
        print(key,value)

displayinfo(chap1 = 10 , chap2 = 20)