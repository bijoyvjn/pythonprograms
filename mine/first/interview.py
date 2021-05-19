import re
num=input("enter the id")
print(num)
x='[1]\d{4}\s\d{2}'
matcher=re.fullmatch(x,num)
if matcher is not None:
    print("product have 10% discount")
    n=int(input("Enter the number of products"))
    sum=n*50
    dis=(sum*10)/100
    print("discount is :",dis)
    total=sum-dis
    print("total :",total)
else:
    n=int(input("Enter the number of prouducts"))
    sum=n*100
    print("toal is :",sum)