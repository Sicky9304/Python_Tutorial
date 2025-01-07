import math
a = float(input("Enter the coefficient of a: "))
b = float(input("Enter the coefficient of b: "))
c = float(input("Enter the coefficient of c: "))

#Logic
d = b*b - 4*a*c

if(d>0):
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The equation has two distinct real roots: {root1} and {root2}")

elif(d==0):
    root = -b/(2*a)
    print(f"The equation has one distinct real roots: {root}")

else:
    real_part = root
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"The equation has two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")



