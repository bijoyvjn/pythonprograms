import re

x="[^abc]" #except a,b or c
matcher=re.finditer(x,"abt c@kx")
for match in matcher:
    print(match.start(),":",match.group())