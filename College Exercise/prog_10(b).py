class B:
    def __init__(self, val1:int):
        self.val1 = val1
        print("Class B Object Created..")
    def show(self):
        print(f"Showing Value: {self.val1}")
    def  __del__(self):
        print("Object Deleted..")

b = B(5)
b.show()
del b
    