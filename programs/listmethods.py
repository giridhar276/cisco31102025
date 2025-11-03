alist = [4,5,3,67,32,78,17,67,26]
alist.append(90)  # list.append(object)
print("After appending:",alist)
alist.extend([91,45,23,53])  # list.extend(list)
print("After extending;",alist)
alist.insert(1,100)          # list.insert(index,value)
print("After inserting :", alist)
alist.pop(0)    # list.pop(index) # value at that index will be removed
print("After pop opreation:",alist)
alist.remove(17)  # 17 is removed from the list
print("After removing :",alist)

if 200 in alist:
    alist.remove(200)
    print("After removing:",alist)
else:
    print("not found in list")

alist.reverse()
print("After reversing:",alist)  #print(alist[::-1])
alist.sort()  # ascending order
print("After sorting :",alist)
alist.sort(reverse=True)
print("After sorting in descending order:",alist)


"""
this
is
multline comment
"""

nums = [1,3,4,5,2,6,7,33,77]
l = len(nums)
new=[]
for i in range(0,len(nums)):
    new.append(nums[len(nums)-i-1])
print(new)
