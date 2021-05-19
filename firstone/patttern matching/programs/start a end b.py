import re
n=input("enter string")
x='^a[\w{}\W{}]*b$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")