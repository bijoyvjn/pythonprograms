import re
n="hellooo"
x='\w*'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")