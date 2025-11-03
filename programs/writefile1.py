
#case1: if languages.txt is not existing.. it gets created first
#case1: if langauges.txt is existing... it overwrites the existing content 

fobj = open("languages.txt","w")

fobj.write("python\n")
fobj.write("unix\n")

lang = input("Enter any language:")
fobj.write(lang + "\n")


for val in range(1,10):
    fobj.write(str(val) + "\n")



fobj.writelines(["python","unix","java\n"])


fobj.close()