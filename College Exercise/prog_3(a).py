# Find the Greatest among Three Numbers..

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

#Logic
greatest = a if a>b and a>c else b if b>c and b>a else c

print("\nGreatest Among Three Numbers = ",greatest)