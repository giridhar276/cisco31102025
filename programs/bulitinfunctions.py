
print("hello")

name = input("Enter any text :")
print(name)

for val in range(1,10):
    print(val)

print(list(range(1,10,2)))

val = 10
print(type(val))
print(isinstance(val,int))#True

alist = [10,20,30]
print(len(alist))

print(max(alist))

print(min(alist))

print(sum(alist))


print(id(alist))  # id() is just the address/reference in C lang
######

print(dir(__builtins__))