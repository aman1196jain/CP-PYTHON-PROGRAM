#Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))
if a + b + c != 180:
    print("The angles do not form triangle")
elif a == 90 or b == 90 or c == 90:
    print("The triangle is a Right triangle.")
elif a > 90 or b > 90 or c > 90:
    print("The triangle is an Obtuse triangle.")
else:
    print("This triangle is a acute triangle.")