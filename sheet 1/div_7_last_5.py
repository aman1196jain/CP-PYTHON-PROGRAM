#WAP to check if the number is divisible by 7 or if the last digit is 5. 
a = int(input("Enter a number: "))
if a % 7 == 0 or a % 10 == 5:   
    print("The number is either divisible by 7 or the last digit is 5.")
else:
    print("The number is neither divisible by 7 nor does it end with 5.")
    