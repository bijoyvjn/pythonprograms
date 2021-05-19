import re

n=input("enter the string")
x='([a-zA-Z]*\d$)'

match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")