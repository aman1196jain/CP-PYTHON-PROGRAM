# WAP to input three numbers and print the minimum number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 <= num2 and num1 <= num3:
    print("Minimum number is:", num1)
else:
    if num2 <= num3:
        print("Minimum number is:", num2)
    else:
        print("Minimum number is:", num3)