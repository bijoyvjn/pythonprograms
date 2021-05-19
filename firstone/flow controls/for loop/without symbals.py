a=input("enter the string")
dig="qwertyuiopasdfghjklzxcvbnm"
c=" "
for i in a:
    if i in dig:
        c+=i
print(c)