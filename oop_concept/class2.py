class Circle:
    pi = 3.14
    def  __init__(self, radius):
        self.radius = radius
        self.area = self.pi * radius * radius
        
    def circulference(self):
        return 2 * Circle.pi * self.radius
    
circle_1 = Circle(4)
print(circle_1.circulference())

print(circle_1.area)
