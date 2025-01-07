class A:
    def __init__(self):
        print("Class A Object Created..")
        
    def show(self):
        print("Showing Class A")
        
    def __del__(self):
        print("Object Deleted..")

a = A()       
a.show()
del a