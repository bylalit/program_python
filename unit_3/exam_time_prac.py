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

class myClass:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("Sum of three numbers is ", a + b + c)
        elif a != None and b != None:
            print("Sum of two numbers is ", a + b)
        else:
            print("Please enter 2 or 3 arguments")
            
m = myClass()
m.sum(10, 20)
m.sum(10, 20, 30)
m.sum(10)