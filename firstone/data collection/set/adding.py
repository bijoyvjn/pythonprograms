s=set()
n=int(input("enter the range"))
for i in range(0,n):
    num=int(input("enter the number"))
    while(num not in s):
        s.add(num)
print(s)