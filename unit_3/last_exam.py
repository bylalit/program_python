# 1
# class student:
#     def __init__(self):
#         self.name = "Rakesh"
#         self.age = 20
#         self.marks = 89
        
#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Marks: ", self.marks)
        
# student = student()
# student.display()



# 2 

# class student:
#     def __init__(self, name, ag=15, m=0):
#         self.name = name
#         self.ag = ag
#         self.m = m
        
        
#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.ag)
#         print("Marks: ", self.m)
        

# stud = student("Rakesh", 20, 52)
# stud.display()



# class sampal:
#     var = 10
#     @classmethod
    
#     def new_modify(cls):
#         cls.var += 1
        
# s1 = sampal()
# s2 = sampal()
# print("X in s1: ", s1.var)
# print("X in s2: ", s2.var)

# s1.new_modify()
# print("X in s1: ", s1.var)
# print("X in s2: ", s2.var)


# class sampal:
#     def __init__(self):
#         self.x = 10
        
#     def modify(self):
#         self.x += 1
        
# s1 = sampal()
# s2 = sampal()
# print("X in s1: ", s1.x)
# print("X in s2: ", s2.x)

# s1.modify()
# print("X in s1: ", s1.x)
# print("X in s2: ", s2.x)





# 4 
# class student:
#     def setname(self, name):
#         self.name =name
        
#     def getname(self):
#         return self.name
    
#     def setmarks(self, marks):
#         self.marks = marks
        
#     def getmarks(self):
#         return self.marks
    
# n = int(input("How many students ?: "))
# i= 0

# while i < n:
#     s = student()
#     name = input("Enter Your name: ")
#     s.setname(name)
#     marks = int(input("Enter Your marks: "))
#     s.setmarks(marks)
#     print("Hii ", s.getname())
#     print("Your Marks : ", s.getmarks())
    
#     i += 1
#     print("------------------------------------------")







