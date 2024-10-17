class Human(object):
    def eat(self):
        print("I can eat")    
    def work(self):
        print("I can work")
        
class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
        
class Boy(Male):
    def work(self):
        # super().work()
        Human.work(self)
        print("I can work for coding")

boy_1 = Boy()
# boy_1.eat()
# boy_1.sleep()

boy_1.work()