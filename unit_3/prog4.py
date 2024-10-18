class Student:
    def setName(self, name, marks):
        self.name = name
        self.marks = marks
    def getName(self):
        print(self.name)
        print(self.marks)
    
    # def setMarks(self, marks):
    #     self.marks = marks
    # def getMarks(self):
    #     return self.marks
    
    
n = int(input("How many Students? "))
i = 0
while i < n:
    s = Student()
    name = input("Enter your Name: ")
    marks = int(input("Enter your Marks: "))
    s.setName(name, marks)
    # s.setMarks(marks)
    s.getName()
    # print("Your Marks: ", s.getMarks())
    i += 1
    print("-----------------------------")
        