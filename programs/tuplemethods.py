

atup = (10,20,30)
#atup[0] = 100
print(atup)


# typecasting - converting from one object to another object
atup = (10,20,30)
alist = list(atup) #step1: converting to list
alist.append(40)   #step2: making changes in the list
atup = tuple(alist)#step3: reconverting back to tuple
print(atup)
######## tuple has 2 methods only ###############
getcount = atup.count(10)  # count the no. of occurences
print(getcount)
getindex = atup.index(30)
print(getindex)

