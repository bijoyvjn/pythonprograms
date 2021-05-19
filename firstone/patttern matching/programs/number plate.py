import re
n=input("enter number")
x='[K][L]\d{2}[A-Z]{1}[0-9]{4}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")