import re

x='a{2,3}'   #minimum 2 maxium 3
matcher=re.finditer(x,"aaa agb aaaa aa ic aat")
for match in matcher:
    print(match.start(), ":", match.group())