
book = {"chap1":10 ,"chap2":20 ,"chap3":30 ,"chap1":100}
print(book)

# display individual value
print(book["chap1"])  #10
print(book["chap2"])  # 20
print(book["chap3"])  # 30

# add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print("updated dictionary :",book)

# dictionary methods 
print("**** display keys *** ")
print(book.keys())

for key in book.keys():
    print(key)

for key in book:
    print(key)


print("**** display values *** ")
print(book.values())

for value in book.values():
    print(value)

print("**** display items *** ")
print(book.items())

for k,v in book.items():
    print("Key :",k)
    print("Value:",v)


book.pop("chap1")  # chap1-10 will be  removed from dictionary
print("After pop opreation :",book)

book.popitem()   # last inserted key-value will be removed
print(book)
book.popitem()
print(book)
#### combining two dictionaries - method1
book = {"chap1":10 ,"chap2":20}
newbook = {"chap3":30 ,"chap4":40}
finalbook = {**book,**newbook}
## updating the same dictionary
book.update(newbook)
print(book)







