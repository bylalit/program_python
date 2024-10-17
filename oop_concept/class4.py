class Human:
    def __init__(self):
        self.num_eyes = 2
        self.noise = 1
    
    def eat(self):
        print("I am eat")
    def work(self):
        print("I acn work")
    
    
class Male:
    def __init__(self, name):
        self.name = name
    
    def flirt(self):
        print("I can fliert")
    def work(self):
        print("I acn coding")
    
# class Female():
#     pass

class Boy(Human, Male):
    def __init__(self, names):
        Human.__init__(self)
        Male.__init__(self, names)
    
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can Testing")

boy_1 = Boy("Lalit")
# boy_1.eat()
# boy_1.flirt()
# boy_1.work()
# print(Boy.mro())

# Human.work(boy_1)


print(boy_1.name)