
# string is immutable
name = "python programming"
print(name)
print("I love", name)
# slicing
# string[start:stop:step]
print(name[0])
print(name[1])
print(name[0:10])
print(name[0:18])
print(name[0:18:1])
print(name[0:18:2])
print(name[::])
print(name[:])
print(name[4:10:2])
print(name[-1])
print(name[-5:-1])
print(name[::-1])

name = "python programming"
print(name.capitalize())
print(name.title())
print(name.upper())
print(name)
print(name.isupper()) # vlidate whether is upper or not
print(name.lower())   # display the string in lower
print(name.islower()) # validate whether string is lower or not
print(name.isalpha()) # only alphas
print(name.isalnum()) # either alphabets or numerics
print(name.split())   # space is the default delimter
print(name.replace("python","unix"))
print(name.count("p"))
print(name.count("program"))
print(name.find("pro")) # check for substring # if found.. it returns index
print(name.find("xyz")) # if not found.. it return -1

string = "I love {} and {}"  #string template
print(string.format("Bangalore","Hyd"))
print(string.format("python","java"))
print(string.format(1,2))
## using f-string style
first_city = "Hyderabad"
second_city = "Bangalore"
print(f"I love {first_city} and {second_city}")

name = " python  "
print(len(name))
print(name.strip())    # remove whitespaces at both ends
print(len(name.lstrip()))  # only at left side
print(len(name.rstrip()))  # only at right side

### converting string to list
name = "python programming"
print(name.split())  # default delimter is space
# converting list to string
alist = ["python","unix"]
print(" ".join(alist))


# conditions



if 1 < 2:
    print("true")

name = "python programing"
if name.isupper():
    print("string is upper")
else:
    print("string is lower")

# check whether pro is existing or not
if name.find("pro") != -1:
    print("substring found")
else:
    print("not found")

if "pro" in name:
    print("substring found")
else:
    print("not found")



## iterating numbers 1 to 9
for i in range(1,10):
    print(i)

# iterating one by one character
name = "python"
for char in name:
    print(char)

alist =[10,20,30]
for char in alist:
    print(char)


# write a program to reverse the string 
#  without using ::-1 and l.reverse()  and without range()
    
input: python
output : nohtyp













































