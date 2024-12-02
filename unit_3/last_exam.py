# 1
# class student:
#     def __init__(self):
#         self.name = "Rakesh"
#         self.age = 20
#         self.marks = 89
        
#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Marks: ", self.marks)
        
# student = student()
# student.display()



# 2 

# class student:
#     def __init__(self, name, ag=15, m=0):
#         self.name = name
#         self.ag = ag
#         self.m = m
        
        
#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.ag)
#         print("Marks: ", self.m)
        

# stud = student("Rakesh", 20, 52)
# stud.display()



# class sampal:
#     var = 10
#     @classmethod
    
#     def new_modify(cls):
#         cls.var += 1
        
# s1 = sampal()
# s2 = sampal()
# print("X in s1: ", s1.var)
# print("X in s2: ", s2.var)

# s1.new_modify()
# print("X in s1: ", s1.var)
# print("X in s2: ", s2.var)


# class sampal:
#     def __init__(self):
#         self.x = 10
        
#     def modify(self):
#         self.x += 1
        
# s1 = sampal()
# s2 = sampal()
# print("X in s1: ", s1.x)
# print("X in s2: ", s2.x)

# s1.modify()
# print("X in s1: ", s1.x)
# print("X in s2: ", s2.x)





# 4 
# class student:
#     def setname(self, name):
#         self.name =name
        
#     def getname(self):
#         return self.name
    
#     def setmarks(self, marks):
#         self.marks = marks
        
#     def getmarks(self):
#         return self.marks
    
# n = int(input("How many students ?: "))
# i= 0

# while i < n:
#     s = student()
#     name = input("Enter Your name: ")
#     s.setname(name)
#     marks = int(input("Enter Your marks: "))
#     s.setmarks(marks)
#     print("Hii ", s.getname())
#     print("Your Marks : ", s.getmarks())
    
#     i += 1
#     print("------------------------------------------")







# class student:
#     marks = 10
#     @classmethod
    
#     def modify(cls, name):
        
#         print(" {} scored {} marks".format(name, cls.marks))
        
# student.modify("Lalit")
# student.modify("Rakesh")





# 1

# x = [24, 27, 30, 18, 17]
# print("Origanal Array: ", x)

# y = []
# y[:] = x
# print("New Array: ", y)


# 2
# import array as arr

# a = arr.array('i', [1,2,3,4,5])
# print(a)

# a[0] = 7
# print(a)

# a[0:2] = arr.array('i', [8,9])
# print(a)

# 3

# list1 = [1,2,3,4,3,5,6,7,3]

# list1.append(8)
# print("Append method: ", list1)

# list1.insert(2, 9)
# print("Insert method: ", list1)

# list1.remove(5)
# print("Remove method: ", list1)

# list1.pop(4)
# print("Pop method: ", list1)

# print(list1.index(3))
# print(list1.count(3))


# import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr.tolist())






# 5 
# list1 = ['hello', 'a','b','c']
# print(list1)

# position = list1.index(input("Enter element for aboue list: "))
# print(position)


# 6

# def test_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if(num % i) == 0:
#                 print(num, "is not a prime number")
#                 break
#             else:
#                 print(num, "is a prime number")
#                 break
                
#     else:
#         print(num, "is not a prime number")
        
# test_prime(18)




# 7 
# list1 = [1,2,3,4,1,2,5,6,4,8,6,9,8,0,3]
# list2 = []

# for i in list1:
#     if i not in list2:
#         list2.append(i)
        
# print(list2)


# 8
# def display_list(list1):
#     for i in list1:
#         print(i)
        
# list1 = [1,2,3,4,5,6]
# display_list(list1)


# 10
# def var_length(*args):
#     for val in range(0, len(args)):
#         print(args[val])
#         print(val)
        
# var_length('a','b','c','d')



# 11
# val = lambda x,y:max(x,y)
# print(val(120,150))


# 12
# def plue_one(num):
#     def add_one(num):
#         return num + 3
#     result = add_one(num)
#     return result

# print(plue_one(10))



# 14

# list1 = [i for i in range(0, 9)]
# print(list1)

# list1.append(22)
# print("Append method: ", list1)

# list1.insert(1, 88)
# print("Append method: ", list1)

# list1.remove(7)
# print("Append method: ", list1)



# 15

# list1 = [i for i in range(1,6)]
# list2 = [i for i in range(7,11)]

# print(list1)
# print(list2)

# list3 = list1 + list2
# print(list3)

# # new_list = [i for i in list3 for x in (0,1)]
# # print(new_list)

# list_clone = list3[:]
# print(list_clone)





# 17

# list1 = [[1,2,3], [4,5,6], [7,8,9]]

# for x in list1:
#     # print(x)
#     print(" ".join(map(str, x)))



# 18

# tup = (1,2,3,4,5,6,7,8)

# print("Max", max(tup))
# print("Min", min(tup))
# print("Sum", sum(tup))
# print("Avg", sum(tup) / len(tup))


# 19

# tup = [(1,(2,3)), (3, (2,1)), (2, (2,1))]

# sort = sorted(tup, key=lambda t: (t[1][1], t[0]))
# print(sort)




# 20

# my_dict = {'name': 'Lalit', 'age': 20}
# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict['address'])



# 21

# keys = ['Cricket', 'BasketBall', 'Hockey']
# values = ['11', '5', '11']

# combine_dict = dict(zip(keys, values))
# print(combine_dict)



# 22

# def func(d):
#     for key in d:
#         print("Key:", key , 'Values: ', d[key])
        
# D = {'a':1, 'b':2, 'c':3}
# func(D)





# 6

# class myclass:
#     n = 0
    
#     def __init__(self):
#         myclass.n += 1
        
#     @staticmethod
#     def no_of_obj():
#         print("No of instances created are: ", myclass.n)
        
        
# obj1 = myclass()
# obj2 = myclass()
# obj3 = myclass()

# myclass.no_of_obj()



# # 7
# import sys

# class bank(object):
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdrow(self, amount):
#         if amount > self.balance:
#             print("Low Balance, Can not withdrow")
#         else:
#             self.balance -= amount
#             return self.balance
        
# name = input("Enter Name: ")
# b = bank(name)

# while True:
#     print("d/D -deposit, w/W -withdrawal, e/E -exit")
#     choice = input("Enter your choice: ")
#     if choice == 'e' or choice == 'E':
#         sys.exit()
        
#     amount = float(input("Enter amount: "))
    
#     if choice == 'd' or choice == 'D':
#         print("Balance After deposite: ", b.deposit(amount))
#     elif choice == 'w' or choice == 'W':
#         print("Balance after withdrawals: ", b.withdrow(amount)) 
        
        
        
# unit 1

# 1
# a = 10
# b = 20

# a = a+b
# b = a -b
# a = a-b

# print(a)
# print(b)

# 2
# print("Enter two compalex number in form of a + bj: ")

# n1 = complex(input())
# n2 = complex(input())

# print("Sum = ", n1 + n2)


# 3
