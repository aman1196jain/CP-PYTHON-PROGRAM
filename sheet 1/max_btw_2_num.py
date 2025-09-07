a=int(input("enter a number: "))
b=int(input("enter another number: "))
if a > b:
    print("The maximum number is:", a)
elif b > a:
    print("The maximum number is:", b)
else:
    print("Both numbers are equal:", a)