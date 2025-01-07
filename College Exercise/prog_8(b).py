import random
import numpy as np
A = []
B = []
m = int(input("Enter the number of rows for matrix A(m): ")) 
n = int(input("Enter the number of columns for matrix B(n): "))
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input("Enter element for A[{}][{}]: ".format(i, j))))
    A.append(row)
print("Matrix A:",A)
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,20))
    B.append(row)
print("Matrix B:",B)
result = np.dot(A, B)
for r in result:
    print("Resultant Matrix: \n",r)