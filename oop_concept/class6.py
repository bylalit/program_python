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
female_1.showDetailes()
# female_1.work()
# female_1.eat()

# male_1 = Male()
# male_1.eat()
# male_1.sleep()
