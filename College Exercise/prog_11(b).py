# import numpy as np
# from sympy import isprime

def isprime(n):
    for i in range(2,int(n ** 0.5) + 1):
        if(n%i == 0):
            return False
    return True
def store_prime_in_file(n,filename = 'prime.txt'):
    primes = []
    num = 2
    while len(primes) < n:
        if isprime(num):
            primes.append(num)
        num+=1
    with open(filename,'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')      
    print(f"First {n} primes have been written to {filename}")
        
n = int(input("Enter the no of prime number to store: "))
store_prime_in_file(n)
