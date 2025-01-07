st1 = input("Enter first statement: ")
st2 = input("Enter second statement: ")

words1 = set(st1.split())
words2 = set(st2.split())

common_words = words1.intersection(words2)

all_unique_words = words1.union(words2)

unique_in_first = words1.difference(words2)

print("Common words: ", common_words)
print("All unique words: ", all_unique_words)
print("Unique words in first statement: ", unique_in_first)