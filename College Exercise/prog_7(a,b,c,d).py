# A. Write a recursive function fibo_n(), which will take an integer as input(n) and returns the n-th term of Fibonacci Series. Make sure
# that the default value of n is 1.

# B. Write a recursive function fibo_s(), which will take an integer as input(n) and show the Fibonacci Series up to n-terms. Make sure that the default value of n is 1.

# C. Use the concept of high-ordered filter function to generate a list of all prime numbers in the range 251 to 5500, in reverse order.

# D. Use the concept of lambda function list all the Leap years in the range 2024 to 3010.

# A. Recursive function to find the n-th term of Fibonacci Series
def fibo_n(n=1):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_n(n-1) + fibo_n(n-2)

# B. Recursive function to show the Fibonacci Series up to n-terms
def fibo_s(n=1, a=0, b=1, series=None):
    if series is None:
        series = []
    if n <= 0:
        return series
    series.append(a)
    return fibo_s(n-1, b, a+b, series)

# C. High-order filter function to generate a list of all prime numbers in the range 251 to 5500, in reverse order
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = list(filter(is_prime, range(251, 5501)))[::-1]

# D. Lambda function to list all the Leap years in the range 2024 to 3010
leap_years = list(filter(lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0), range(2024, 3011)))

# Call the functions and print the results

# A. Call fibo_n() and print the n-th term of Fibonacci Series
n = 10
print(f"The {n}-th term of the Fibonacci Series is: {fibo_n(n)}")

# B. Call fibo_s() and print the Fibonacci Series up to n-terms
n = 10
print(f"The Fibonacci Series up to {n} terms is: {fibo_s(n)}")

# C. Print the list of all prime numbers in the range 251 to 5500, in reverse order
print(f"Prime numbers in the range 251 to 5500 in reverse order: {prime_numbers}")

# D. Print the list of all Leap years in the range 2024 to 3010
print(f"Leap years in the range 2024 to 3010: {leap_years}")