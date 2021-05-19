list=[1,2,3,4,5,6,7,8,9]
p=[]
n=[]
for i in list:
    if(i>1):
        for j in range(2,i):
            if i%j==0:
                n.append(i)
                break
            else:
                p.append(i)
print("prime numbers",p)
print("non prime numbers",n)