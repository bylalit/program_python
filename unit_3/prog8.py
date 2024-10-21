class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.salary = sal
        
    def display(self):
        print("Id = ", self.id)
        print("Name = ", self.name)
        print("Salary = ", self.salary)
        
class myClass:
    @staticmethod
    def myMethod(e):
        e.salary += 1000
        e.display()
        
f = Emp(1, "Rahul", 5000)
myClass.myMethod(f)



# class Emp:
#     def __init__(self, id, name, sal):
#         self.id = id
#         self.name = name
#         self.salary = sal
        
#     def display(self):
#         print("Id = ", self.id)
#         print("Name = ", self.name)
#         print("Salary = ", self.salary)
        
# class myClass:
#     @classmethod
#     def myMethod(cls, e):
#         e.salary += 1000
#         e.display()
        
# f = Emp(1, "Rahul", 5000)
# myClass.myMethod(f)
            
