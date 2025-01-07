# Second MAX and Second MIN of a list

L = list(map(int, input("Enter the list elements: ").split()))
new_list = [0] * (max(L) + 1)
for i in L:
    new_list[i] = i
print(new_list)