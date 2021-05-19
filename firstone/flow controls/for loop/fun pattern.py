def pattern():
    for i in range(1,6):
        print()
        for j in range(6,i,-1):
            print("*",end=" ")

pattern()