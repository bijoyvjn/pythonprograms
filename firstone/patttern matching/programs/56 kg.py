import re

n="56 kg"
x='\d{2}\s\w{2}'

match=re.fullmatch(x,n)

if match is not None:
    print("valid")
else:
    print("Invalid")