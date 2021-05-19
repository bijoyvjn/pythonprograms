n=int(input("enter the range"))
a=0
b=1
count=0
print(a)
print(b)
for i in range(0,n+1):
        count+=i
        if(count>=n):
            c=a+b
            a=b
            b=c
            print(c)