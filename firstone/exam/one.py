lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
lst.sort()
for i in lst:
    for j in lst:
        if i==j:
            lst.remove(j)
print(lst)