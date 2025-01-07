# sorting list of strings by last character
# using lambda function

string = input("Enter the strings separated by space: ").split()
string.sort(key = lambda x: x[-1])
print(string)


