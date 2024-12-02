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







# class student:
#     marks = 10
#     @classmethod
    
#     def modify(cls, name):
        
#         print(" {} scored {} marks".format(name, cls.marks))
        
# student.modify("Lalit")
# student.modify("Rakesh")





# 1

# x = [24, 27, 30, 18, 17]
# print("Origanal Array: ", x)

# y = []
# y[:] = x
# print("New Array: ", y)


# 2
# import array as arr

# a = arr.array('i', [1,2,3,4,5])
# print(a)

# a[0] = 7
# print(a)

# a[0:2] = arr.array('i', [8,9])
# print(a)

# 3

list1 = [1,2,3,4,3,5,6,7,3]

# list1.append(8)
# print("Append method: ", list1)

# list1.insert(2, 9)
# print("Insert method: ", list1)

# list1.remove(5)
# print("Remove method: ", list1)

# list1.pop(4)
# print("Pop method: ", list1)

# print(list1.index(3))
# print(list1.count(3))


# import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr.tolist())