class Human:
    def eat(self):
        print("Human is eating")
        
    def work(self):
        print("Human is working")
        
class Male(Human):
    def flirt(self):
        print("Male is flirting")
        
    def work(self):
        print("I can working coding")

male_1 = Male()
male_1.flirt()
male_1.work()