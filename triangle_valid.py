# You have given three integer angles of a triangle. Check if the triangle is valid or not.

ang1 = int(input("enter fist angle: "))
ang2 = int(input("enter second angle :"))
ang3 = int(input("enter third angle :"))
if ang1 + ang2 + ang3 == 180:
    print("Triangle is valid")
else:
    print("Triangle is not valid")