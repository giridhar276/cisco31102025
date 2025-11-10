# set is UNORDERED collection of UNIQUE elements of same type.
aset = {10,20,20,20,30,30,30}
print(aset)
bset = {30,30,30,40,40,50,50}
print(bset)

print(aset.union(bset))  # {10,20,30,40,50}

print(aset.intersection(bset))  # {30}

print(aset.difference(bset))    # {10,20}

print(bset.difference(aset))    #{40,50}

print(aset.issubset(bset))
print(aset.issuperset(bset))

aset.add(40)
print(aset)
print(bset)



languages = {"python","java","c","cpp"}
languages.discard("python")
print(languages)
languages.discard("python1111")  # no error  # s.discard() is safe
print(languages)

languages = {"python","java","c","cpp"}
languages.remove("python")
print(languages)
#languages.remove("python111")
print(languages)


languages = {"python","java","c","cpp"}
removed = languages.pop()
print(removed)