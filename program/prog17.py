# oops in python

# class Student:
#     name = "Karan Kumar"
     
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "blue"
#     brand = "honda"
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)




# class Student:
    
    
#     collage_name = "ABC Collage"   # class attr
    
#     # default constructore
#     def __init__(self):
#         pass
    
#     # parameterized constructore
#     def __init__(self, name, marks):
#         self.name = name          # obj attr
#         self.marks = marks
#         # print("Adding a new student...")
        
# s1 = Student("Lalit", 30)
# print(s1.name, s1.marks)

# s2 = Student("Vidhi", 20)
# print(s2.name, s2.marks)

# print(Student.collage_name)



# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name          # obj attr
#         self.marks = marks
    
#     def welcome(self):
#         print("Welcome student...", self.name)
        
#     def get_marks(self):
#         return self.marks
        
# s1 = Student("Lalit", 30)
# s1.welcome()
# print(s1.get_marks())




# Execise

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg score is: ", int(sum / 3))
        
    
#     @staticmethod
#     def hello():
#         print("hello")
        
# s1 = Student("Lalit", [99, 98, 97])
# s1.get_avg()

# s1.name = "ironman"
# s1.get_avg()

# s1.hello()





# Abstraction

# class Car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
        
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car starting...")
        
# car1 = Car()
# car1.start()




# Execise
# class Account:
#     def __init__(self, bal, acc):
#         self.bal = bal
#         self.acc = acc
        
#     # debit method
#     def debit(self, amount):
#         self.bal -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = ", self.get_balance())
        
#     # credit method   
#     def credit(self, amount):
#         self.bal += amount
#         print("Rs.", amount, "was credited")
#         print("total balance = ", self.get_balance())
        
#     def get_balance(self):
#         return self.bal    
    
    
# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(20000)








# class Student:
#     def __init__(self, name):
#         self.name = name
        
# s1 = Student("Lalit")
# print(s1.name)
# # delete for obj 
# del s1.name



class A:
    varA = "Welcome  to class A"
    
class B:
    varB = "Welcome to class B"
    
class C(A,B):
    varC = "Welcome to class C"
    
c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA) 
