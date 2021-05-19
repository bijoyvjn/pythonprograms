import re

n=input("enter the number to valid")

x='[+][9][1]\d{10}'

match=re.fullmatch(x,n)

if match is not None:
    print("valid")
else:
    print("Invalid")