# input three number and give minimum number by function.

def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num3:
        return num2
    else:
        return num3

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("Minimum number is:", min_num(num1, num2, num3))