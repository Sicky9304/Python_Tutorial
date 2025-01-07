from sympy import isprime
start = int(input("Enter the Starting Range: "))
end = int(input("Enter the Ending Range: "))
count = 0
for n in range(start, end + 1):
    if isprime(n):
        count += 1
        print(n,end= " ")
    
print(f"\n\nPrime numbers between {start} and {end}: ",count)
