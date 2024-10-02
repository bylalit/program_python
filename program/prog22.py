class student:
    def __init__(self, name, age , marks):
        self.name = name
        self.age = age
        self.marks = marks
        
        
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Marks: ", self.marks)
        
s = student("Raj", "20","89")

s.display()

