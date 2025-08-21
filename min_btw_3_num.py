a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a < b and a < c:
    print("The minimum number is:", a)
elif b < a and b < c:
    print("The minimum number is:", b)
elif c < a and c < b:
    print("The minimum number is:", c)
else:
    print("All numbers are equal:", a, b, c)