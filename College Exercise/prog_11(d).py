file_name = 'content.txt'
try:
    with open(file_name,'r') as file:
        print("Content of the file: ")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f'The file {file_name} does not exists..')