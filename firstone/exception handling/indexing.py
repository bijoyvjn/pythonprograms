a=[1,4,2]
n=int(input("enter the elelment"))
try:
    print(a[n])
except:
    print("error")
finally:
    print("inside finally")

    # //finally block work in both try and except cases