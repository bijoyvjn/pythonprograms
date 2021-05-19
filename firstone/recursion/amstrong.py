num=int(input("enter the number"))
sum=0
temp=num
while(num!=0):
    dig=num%10
    sum+=dig*dig*dig
    num//=10
if(temp==sum):
    print("amstrong number")
else:
    print("not an amstrong number")