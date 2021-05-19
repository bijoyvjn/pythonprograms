low=int(input("Enter the number"))
up=int(input("Enter the number"))
osum=0
esum=0
for i in range(low,up+1):
    if(i%2==0):
        esum=esum+i
    else:
        osum=osum+i
print("odd sum",osum)
print("even sum",esum)
