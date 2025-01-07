try:
    with open('content.txt','w') as file:
        file.write("Hello welcome to python programming ... \nLets learns the new things with the help of python and file handling function...")
    print(f"The text written Successfully to {'content.txt'}..")

except Exception as e:
    print(e)