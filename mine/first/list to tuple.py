lst=[]
size=int(input("enter the size"))
for i in range(0,size):
    num=int(input("enter the numbet to be add"))
    lst.append(num)
print(" the list is ",lst)
tuple=tuple(lst)
print(tuple)