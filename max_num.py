#Read three integers and print their maximum. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
print("Maximum number is:", max_num(a, b, c))
    