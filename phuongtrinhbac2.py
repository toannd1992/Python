# Giai phuong trinh bac 2
# ax2 +bx + c = 0
import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

delta = b * b - (4 * a * c)


if (a != 0):
    if (delta < 0):
        print("Phuong trinh vo nghiem")
    elif (delta > 0):
        x1 = (-b + math.sqrt(delta))/ (2 * a)
        x2 = (-b - math.sqrt(delta))/ (2 * a)
        print("X1 =", x1)
        print("X2 =", x2)
    else:
        x1 = (-b + math.sqrt(delta))/ (2 * a)
        print("X1 = X2 =", x1)
else:
    if (b != 0):
        print("phuong trinh co x =", -c/b)
    else:
        if (c == 0):
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")