lst=[7,8,9,4,3,1]
a=[]
b=[]

# print("positions",end=' ')
for i in lst:
    ind=lst.index(i)
    # print(ind,end=' ')
    while ind<4:
        i+=1
        a.append(i)
        break
    while ind>=4:
        i-=1
        b.append(i)
        break
# print()
print("old list",lst)
a.extend(b)
print("new list",a)