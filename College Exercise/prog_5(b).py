# Extract Rool no and Institute Name..

email = input("Enter the Email Id: ")
roll,institute_name = email.split("@")
institute_name = institute_name.split(".")[0]
print("Roll Number: ",roll)
print("Institute Name: ",institute_name.upper())