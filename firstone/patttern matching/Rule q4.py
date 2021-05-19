import re

x='a{3}'   # count how many three a are together
matcher=re.finditer(x,"aaa agb aaaa aa ic aat")
for match in matcher:
    print(match.start(), ":", match.group())