# Accept the percetage of marks obtained by a student and print the grade based on the following criteria:
per1 = float(input("Enter the percentage of marks obtained: "))
if per1 >= 90:
    print("Grade: A")
elif per1 >= 80:
    print("Grade: B")
elif per1 >= 70:
    print("Grade: C")
elif per1 >= 60:
    print("Grade: D")
elif per1 >= 50:
    print("Grade: E")
else:
    print("Grade: F")