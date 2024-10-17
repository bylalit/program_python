class Human:
    def eat(self):
        print("I am eat")
    def work(self):
        print("I acn work")
    
    
class Male:
    def flirt(self):
        print("I can fliert")
    def work(self):
        print("I acn coding")
    
class Boy(Human, Male):
    pass

boy_1 = Boy()
# boy_1.eat()
# boy_1.flirt()
# boy_1.work()

Human.work(boy_1)