# pro 18

# import math 
# class square:
#     def area(self, x):
#         print("Area of Square = ", x * x)
        
# class circle(square):
#     def area(self, x):
#         print("Area of Circle =", math.pi * x * x)
        
# c = circle()
# c.area(5)


# pro 17

# class myClass:
#     def sum(self, a=None, b=None, c=None):
#         if a != None and b != None and c != None:
#             print("Sum of three numbers is ", a + b + c)
#         elif a != None and b != None:
#             print("Sum of two numbers is ", a + b)
#         else:
#             print("Please enter 2 or 3 arguments")
            
# m = myClass()
# m.sum(10, 20)
# m.sum(10, 20, 30)
# m.sum(10)


# # pro 16

# class bookx:
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):
#         return self.pages + other.pages
    
# class booky:
#     def __init__(self, pages):
#         self.pages = pages
        
# b1 = bookx(100)
# b2 = booky(200)
# print("Total Pages: ", b1 + b2)


# pro 15

# class dog:
#     def bark(self):
#         print("Bow Bow")

# class duck:
#     def talk(self):
#         print("Quack Quack")
        
# class human:
#     def talk(self):
#         print("Hello, Hii") 
        
        
# def call_talk(obj):
#     if hasattr(obj, "talk"):
#         obj.talk()
#     elif hasattr(obj, "bark"):
#         obj.bark()
#     else:
#         print("Wrong object Passed")
        
# x = duck()
# call_talk(x)

# x = human()
# call_talk(x)






# pro 14

class a:
    def method(self):
        print("A class method")
        super().method()
class b:
    def method(self):
        print("B class method")
        super().method()
class c:
    def method(self):
        print("C class method")
        super().method()
class x(a,b):
    def method(self):
        print("X class method")
        super().method()
class y(b,c):
    def method(self):
        print("Y class method")
        super().method()
        super().method()
class p(x,y,c):
    def method(self):
        print("P class method")
        super().method()
        
        
p1 = p()
print(p.mro())
p1.method()