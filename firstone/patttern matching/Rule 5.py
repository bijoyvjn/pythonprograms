import re

x='[a-zA-Z]'   #a to z and A to Z
matcher=re.finditer(x,"ADFGagdd")
for match in matcher:
    print(match.start(), ":", match.group())