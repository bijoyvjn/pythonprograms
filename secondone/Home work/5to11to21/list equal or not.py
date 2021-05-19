lst1=[10,20,21,22,23]
lst2=[20,21,10,22,23]
flag=0
for i in lst1:
    if i in lst2:
        flag+=0
    else:
        flag+=1
if flag==0:
    print("equal")
else:
    print("not equal")