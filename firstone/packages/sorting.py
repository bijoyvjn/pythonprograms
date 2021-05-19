def sort():
    a=[11,5,4,7,6,9,8]
    b=[]
    print("unsorted list",a)
    for i in a:
        for j in a:
            while(i<j):
                b.append(i)
                i+=1
                j+=2
    print(b)
sort()
