# Accept the sentence and count the upper and lower case character..

sentence = str(input("Enter the sentence: "))
upper = sum(1 for char in sentence if char.isupper())
lower = sum(1 for char in sentence if char.islower())
print("UpperCase Letters: ",upper)
print("LowerCase Letters: ",lower)