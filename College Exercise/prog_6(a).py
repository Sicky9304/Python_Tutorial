# Second MAX and Second MIN of a list

lists = list(map(int, input("Enter the numbers in list: ").split()))
lists.sort()
print("Second MAX: ", lists[-2])
print("Second MIN: ", lists[1])