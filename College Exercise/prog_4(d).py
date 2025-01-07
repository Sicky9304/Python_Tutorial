# Generate Pattern 1

# n = int(input("Enter the no of lines: "))
# for i in range(1,n):
#     print("*" * i)
# print("*" * (n*2-1))
# for j in range(n,1,-1):
#     print(" " * (2*n-j) + "*" * (j-1))


# Generate Pattern 2

for i in range(65,70):
    for k in range(70-i):
        print(" ",end=" ")
    for j in range(i,64,-1):
        print(chr(j),end=" ")
    print()
