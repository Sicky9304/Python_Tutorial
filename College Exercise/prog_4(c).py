# Print Automorphic Numbers..

start = int(input("Enter the Starting Range: "))
end = int(input("Enter the Ending Range: "))
for n in range(start,end):
    square = str(n ** 2)
    num_str = str(n)

    if square.endswith(num_str):
        print(f"{n} is an automorphic number.")

