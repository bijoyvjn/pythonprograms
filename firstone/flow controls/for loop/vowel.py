a=input("enter the string")
vow="aeiou"
count=0
for i in a:
    if i in vow:
        count+=1
print(count)
