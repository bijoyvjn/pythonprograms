total={"anu","chala","chittu","tuttu","cheru","bijoy"}
print("total students",total)
fail={"anu","chala"}
print(fail)
s=set()

for i in total:
     if i not in fail:
         s.add(i)
print(s)