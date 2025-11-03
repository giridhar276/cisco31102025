

name = input("Enter any name :")
print(name)
revstr = ""
for char in name:
    revstr = char + revstr
print("String reverse:", revstr)


# range(start,stop,step)  # range(6,-1,-1)
for char in range(len(name)-1,-1,-1):
    print(name[char],end="")