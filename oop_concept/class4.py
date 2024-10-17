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
    
# class Female():
#     pass

class Boy(Human, Male):
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can Testing")

boy_1 = Boy()
# boy_1.eat()
# boy_1.flirt()
boy_1.work()
print(Boy.mro())

# Human.work(boy_1)