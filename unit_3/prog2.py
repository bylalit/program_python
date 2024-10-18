class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        
    def display(self):
        print("Name is: ", self.name)
        print("Age is: ", self.age)
        print("Marks is: ", self.marks)
    
s = Student("Lalit", 18, 90)
s.display()
print()
print()
s1 = Student("Mittal", 18, 90)
s1.display()