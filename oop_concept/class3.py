class Human:
    def __init__(self):
        self.num_eyes = 2
        self.nose = 1
        
    def eat(self):
        print("Human is eating")
        
    def work(self):
        print("Human is working")
        
class Male(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def flirt(self):
        print("Male is flirting")
        
    def work(self):
        super().work()
        print("I can working coding")

print()
male_1 = Male("Lalit")
# male_1.flirt()
# male_1.work()
# print(male_1.num_eyes)
print(male_1.name)
print()