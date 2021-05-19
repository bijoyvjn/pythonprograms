w=input("enter the string")
temp=w
for i in w:
    rev=w[::-1]

if(temp==rev):
    print("palindrome")
else:
    print("not a palindrome")

