class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def showDetailes(self):
        print(f"My name is {self.name}, and age is {self.age}.")
            
    def eat(self):
        print("Human is eating")
        
class Male(Human):
    def sleep(self):
        print("I can sleep")
    
class Female(Human):
    def work(self):
        print("I can work")
        
female_1 = Female("lalit", 18)
# female_1.showDetailes()
# female_1.work()
# female_1.eat()

# male_1 = Male()
# male_1.eat()
# male_1.sleep()




class A:
    def dispaly(self):
        print("Inside class A")
        
class B(A):
    def dispaly(self):
        print("Inside class B")
        
class C:
    def dispaly(self):
        print("Inside class C")

class D(B,C):
    def dispaly(self):
        print("Inside  class D")
        
d1 = D()
d1.dispaly()
# print(D.mro())
    


