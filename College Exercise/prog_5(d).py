sentence = input("Please enter a sentence: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
substring = sentence[start:end+1]
print("Extracted substring: ",substring)

clean_substring = "".join(e for e in substring if e.isalnum()).lower()
print("Cleaned substing: ",clean_substring)

if (clean_substring == clean_substring[::-1]):
    print(f"{substring} is a palindrome.")
else:
    print(f"{substring} is not a palindrome.")
