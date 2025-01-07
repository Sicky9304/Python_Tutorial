# Swap without using third variable..

a = int(input("Enter the First No: "))
b = int(input("Enter the second No: "))

print("\nBefore Swapping A , B = ",a,b)
# Logic
a,b = b,a
print("After Swapping A , B = ",a,b)

print("\n ************************")

# Swap with using third variable..

print("Before Swapping A , B = ",a,b)

# Logic
temp = a
a = b
b = temp

print("After Swapping A , B = ",a,b)



