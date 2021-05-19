a=input("enter the string")
b=input("enter the letters")
count=0
for i in a:
    if i in b:
        count+=1
print(count)