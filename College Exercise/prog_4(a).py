# Generate Fibonacci Series Upto Nth terms..

n = int(input("Enter the no of terms: "))
a,b = 0,1
print("Fibonacci Series: ")
for i in range (n):
    print(a,end=" ")
    a,b = b,a+b