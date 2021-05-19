import re

x='^a'   # check starting with a
matcher=re.finditer(x,"aaa cagb aaaa taa ic aat")
for match in matcher:
    print(match.start(), ":", match.group())