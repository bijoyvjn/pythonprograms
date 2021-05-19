import re

x='[\s]'   # checking for space
matcher=re.finditer(x,"ADFG agdd")
for match in matcher:
    print(match.start(), ":", match.group())