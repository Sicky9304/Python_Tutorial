class B:
    def __init__(self,val1:int):
        self.val1 = val1
        print("Class B Object Created..")
    def show(self):
        print(f"Showing the Value: {self.val1}..")
    def __del__(self):
        print("Object Deleted..")

class C(B):
    def __init__(self,val1:int,val2:int):
        super().__init__(val1)
        self .val2 = val2
        print("Class C object Created..")
    
    def show(self):
        print(f"Showing Class C with {self.val1}, {self.val2}")

c = C(10,20)
c.show()
del c