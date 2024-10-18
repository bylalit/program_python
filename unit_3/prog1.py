class Students:
    def __init__(self):
        self.name = "Lalit"
        self.age = 18
        self.marks = 90
        
    def display(self):
        print("Name is: ", self.name)
        print("Age is: ", self.age)
        print("Marks is: ", self.marks)
        

s1 = Students()
s1.display()