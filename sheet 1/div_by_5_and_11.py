# Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not. 
a = int(input("Enter a number: "))
if a % 5 == 0 and a % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")