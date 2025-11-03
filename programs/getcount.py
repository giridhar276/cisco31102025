str1=input("Enter a String:") # aaabbbccc
d=dict()  # {}
for i in str1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    print(i,":",d[i])


str1=input("Enter a String:")  #aaabbbccc
strlist = list(str1)   # [a,a,a,b,b,b,c,c,c]
print(strlist)
for char in set(strlist):  #[a,b,c]
    print(char, strlist.count(char),"times")