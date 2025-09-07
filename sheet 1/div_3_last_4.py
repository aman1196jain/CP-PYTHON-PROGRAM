#WAP to check if the number is divisible by 3 and the last digit is 4.
a = int(input("Enter a number: "))
if a % 3 == 0 and a % 10 == 4:
    print("The number is divisible by 3 and last digit is 4.")
else:
    print("The number is not divisible by 3 or last digit is not 4.")
