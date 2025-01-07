open_list = ["(", "[", "{"]
close_list = [")", "]", "}"]
def Well_bracketd(string):
    try:
        stack = []
        for char in string:
            if char in open_list:
                stack.append(char)
            elif char in close_list:
                pos = close_list.index(char)
                if ((len(stack) > 0) and 
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
expression = input("Enter an expression: ")
if Well_bracketd(expression):
    print("The brackets are well-formed.")
else:
    print("The brackets are not well-formed.")
    
