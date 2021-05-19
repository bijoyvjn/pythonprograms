# limit
# print prime numbers until that limit


low=int(input("Enter the lowest numbers"))
high=int(input("Enter the highest number"))
sum=0
for a in range(low,high):
    if (a>1):
        for i in range(2,a):
            if(a%i==0):
                break
        else:
            print(a)
            sum+=a
print("sum of prime numbers in",min,"to",max,"is",sum)

