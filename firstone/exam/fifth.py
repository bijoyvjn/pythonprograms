lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
a,b,c=lst
if a[3]>b[3]:
    if a[3]>c[3]:
        print(a)
    else:
        print(c)
elif b[3]>a[3]:
    if b[3]>c[3]:
        print(b)
    else:
        print(c)
else:
    print(c)

