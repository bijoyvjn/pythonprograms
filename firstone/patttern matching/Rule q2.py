import re

x='a*'   #count including zero number of a
matcher=re.finditer(x,"aa agb ic aat")
for match in matcher:
    print(match.start(), ":", match.group())