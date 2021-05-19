import re

x='a$'   #ending with a
matcher=re.finditer(x,"aaa agb aaaa aa ic aa")
for match in matcher:
    print(match.start(), ":", match.group())