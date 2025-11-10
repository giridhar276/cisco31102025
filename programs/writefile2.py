
# traditional way  # regular way
fobj = open("languages.txt","w")
fobj.write("python\n")
fobj.write("unix\n")
fobj.close()

# context manager
# if any starts using 'with' keyword ... it is called as context manager
# Advantage:  file gets closed automatically
with open("languages.txt","w") as fobj:
    fobj.write("python\n")
    fobj.write("test\n")
    



# other areas where the context manager can be used:
# network connections,database connections,socket connections,server