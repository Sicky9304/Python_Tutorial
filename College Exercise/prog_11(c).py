def fibonacci(n):
    a, b = 0, 1
    fib_list = []
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
n = int(input("Enter the Terms for Fibo Sequence: "))        
with open('fibo.txt','w') as file:
    for i in fibonacci(n):
        file.write(str(i) + "\n")
print(f"Fibonacci series up to {n} have been written to {"fibo.txt"}")
