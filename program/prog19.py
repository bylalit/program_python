# random function

# random.randint(2,8)
# random.randrange(2,4)
# random.choice([12,11,10])

# random.random()*5
# random.shuffle([2,4,5,6])
# random.uniform(3,9)


# import random
# import string
# n = random.randint(2,8)
# print(n)

# n1 = random.randrange(2,4)
# print(n1)


# l = [10,20,30,40]
# n2 = random.choice(l)
# print(n2)


# r = random.random()*5   #only 0 and 1 give the value.
# print(int(r))


# l = [10,20,30,40]
# random.shuffle(l)
# print(l)


# u = random.uniform(3,9)     #floating  point number give  the value.
# print(u)







# program 1.
# gusees the  random number between 1 to 100

# target = random.randint(1, 100)

# while True:
#     guess = input("Guess a number between 1 and 100 or Quit(Q): ").upper()
    
#     if guess == "Q":
#         break
    
#     guess = int(guess)
    
#     if guess == target:
#         print("You guessed it!")
#         break
#     elif guess < target:
#         print("Too low!")
#     else:
#         print("To high!")

# print("------GAME OVER------")




# program 2.
# Random password  generator


# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# pass_len = 8
# charValue =  string.ascii_letters + string.digits + string.punctuation

# # password = ""
# # for i in range(pass_len):
# #     password += random.choice(charValue)


# # list comprehension
# password = "".join([random.choice(charValue) for i in range(pass_len)])


# print("your random password is: ", password)





 


#  1. program

# target = random.randint(1,100)

# while True:
#     guss = input("Guess a number between 1 and 100 or Quit(Q): ").upper()

#     if guss == "Q":
#         break
     
#     guss = int(guss)

#     if target == guss:
#         print("You guessed it! The number was indeed", target)
#         break
#     elif  target > guss:
#         print("Too low!")
#     else:
#         print("Too high!")

# print("-----Game Over------")




# d = {
#     'a': 10,
#     'b': 20,
#     'c': 30
# }
# # print(d)

# # print(d.get('b'))
# # print(d.items())
# # print(d.keys())
# print(d.popitem())




# import random

# ques1 = ["name","age","address","number"]
# ans = ["vidhi",20,"amdavad",98]
# # print(ans[0],ans[1])

# for i in ques1:
#     pcount=0

#     # print(i)
#     if i=="name":
#         new = input("write your name=")

#         if new==ans[0]:
#             print("pass")
#             pcount += 1
#             print(pcount)
#         else:
#             print("fail")
#     elif i=="age":
#         new2 = int(input("write age="))
#         if new2 == ans[1]:
#             print("pass")
#             pcount += 1
#             print(pcount)

#         else:
#             print("fail")

#     elif i=="address":
#         new = input("enter address=")
#         if new == ans[2]:
#             print("pass")
#             pcount += 1
#             print(pcount)
#         else:
#             print("fail")

#     elif i == "number":
#         new = int(input("enter number="))
#         if new == ans[3]:
#             print("pass")
#             pcount += 1
#             print(pcount)
#         else:
#             print("fail")

#         print("your marks is",pcount)





ques1 = ["name","age","address","number"]
ans = ["vidhi","20","amdavad","98"]
pcount = 0
loop_num = 0

for i in  ques1:
    answer = input("Enter your answer for "+i+"= ")
    for j in ans:
        print("Your ans: ", answer)
        break
    if ans[loop_num] == answer:
        print("pass")
        pcount += 1
    else:
        print("fail")
        
    loop_num += 1 
    
print("your marks is",pcount)
print("Thank You")
