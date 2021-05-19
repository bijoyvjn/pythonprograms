num=int(input("Enter the number"))
print(num)
sum=0
while(num!=0):
    rem = num % 10
    sum=sum*10+rem
    num = num // 10
print("reversed number",sum)