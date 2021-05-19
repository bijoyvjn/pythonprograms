import re

x='[a-z]'   #a to z
matcher=re.finditer(x,"ADFGagdd")
for match in matcher:
    print(match.start(), ":", match.group())