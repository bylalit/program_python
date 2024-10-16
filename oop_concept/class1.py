class InstructorInfo:
    def __init__(self, name, add):
        # print("Createing new object")
        self.name = name
        self.addes = add
        self.followers = 0

isinstance_1 = InstructorInfo("Jenny", "Delhi")
print(isinstance_1.name)
print(isinstance_1.addes)


isinstance_2 = InstructorInfo("Lalit", "Delhi")
print(isinstance_2.name)
print(isinstance_2.addes)