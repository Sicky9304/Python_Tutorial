import os
file_path = input("Enter the file path: ")
try:
    file = open(file_path,'r')
    file_size = os.path.getsize(file_path)
    print(f'File Size: {file_size}  bytes')
    file.close()
except FileNotFoundError:
    print(f"File not found in the given path {file_path}")
    