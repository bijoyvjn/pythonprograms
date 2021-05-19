import re

x='[^a-zA-Z0-9]'   #special symbols
matcher=re.finditer(x,"ADFG@ag#d&d")
for match in matcher:
    print(match.start(), ":", match.group())