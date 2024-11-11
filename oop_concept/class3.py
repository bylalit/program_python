class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.nose = 1
        self.num_heart = num_heart
        
    def eat(self):
        print("Human is eating")
        
    def work(self):
        print("Human is working")
        
# class Male(Human):
#     def __init__(self, name, heart):
#         super().__init__(heart)
#         self.name = name
        
#     def flirt(self):
#         print("Male is flirting")
        
#     def work(self):
#         super().work()
#         print("I can working coding")
        
#     def diaplay(self):
#         print(f"Hi, I am {self.name} and I have {self.num_heart} heart.")

# print()
# male_1 = Male("Lalit", 2)
# male_1.flirt()
# male_1.work()
# print(male_1.num_eyes)


# print(male_1.name)
# print(male_1.num_heart)
male_1.diaplay()
print()