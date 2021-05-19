import re

x='a?'   #count a as each including zero number of a
matcher=re.finditer(x,"aa agb ic aat")
for match in matcher:
    print(match.start(), ":", match.group())