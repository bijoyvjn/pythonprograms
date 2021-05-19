import re
n=input("enter email")
x='^\w\W[@gmail.com]'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")