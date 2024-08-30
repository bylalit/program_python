# 1  program sum of two numbers using function
# def sum_of_two_numbers(a, b):
#     return a + b
# a = 40
# b = 50
# print("Sum of two numbers is ", sum_of_two_numbers(a, b))





# # 2 program sum of three numbers using function
# def sum_of_three_numbers(a, b, c):
#     return a + b + c
# a = 20
# b = 30
# c = 10
# print("Sum of three numbers is ", sum_of_three_numbers(a, b, c))





# 3 program any character
# def any_character():
#     char = input("Enter any character: ")
#     print("The character you entered is: ", char)
# any_character()





# 4 program full name 
# def full_name():
#     name = input("Enter your fulll name: ")
#     print("Your Full Name is: ", name)
# full_name()





# 5 program swaping without third  variable
# a = 10
# b = 20
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)





# 6 program swapping using third variable
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print(a)
# print(b)





# 7 program average of three number
# a = 70
# b = 80
# c = 50
# avg =  (a + b + c) / 3
# print("The average of three number is: ", int(avg))





# 8 program celcius to ferenhiet
# c = 30
# f = (c * 9/5) + 32
# print("The temperature in ferenhiet is: ", f)





#  9 program ferenhiet to celcius
# f = 86
# c = (f - 32) * 5/9
# print("The temperature in celcius is: ", c)





# 10 program  to find the maximum of two number
# a = 20
# b = 10
# if a > b:
#     print("A is maximum")
# else:
#     print("B is maximum")





# 11 program  to find the maximum of three number
# a = 244
# b = 22
# c = 755
# if a > b:
#     if a > c:
#         print("A is maximum")
#     else:
#         print("C is maximum")
# else:
#     if b > c:
#         print("B is maximum")
#     else:
#         print("C is maximum")


# if a > b and  a > c:
#     print("A is maximum")
# elif b  > a and b > c:
#     print("B is maximum")
# else:
#     print("C ia maximum")





# 12 program eligible for vote or not
# age = 17
# if age >= 18:
#     print("Can you vote")
# else:
#     print("Cant vote now")





# 13 program Positive or negative number
# num = -12
# if num >= 0:
#     print("Positive number")
# else:
#     print("Negative number")





# 14 program even or odd number
# num = 39
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")





# 15 program positive negative or zero
# num = 0
# if num == 0:
#     print("Zero number")
# elif num > 0:
#     print("Positive number")
# else:
#     print("Negative number")





# 16 program grade  of student A++ A B++ B C++ C Fail
# math = 78
# sic = 89
# eng = 59
# hindi = 67
# guj = 79
# total = math + sic + eng + hindi + guj
# avg = total / 5
# print(int(avg))

# if avg >= 90:
#     print("A++ Grade")
# elif avg >= 80:
#     print("A Grade")
# elif avg >= 70:
#     print("B++ Grade")
# elif avg >= 60:
#     print("B Grade")
# elif avg >= 50:
#     print("C++ Grade")
# elif avg >= 40:
#     print("C Grade")
# else:
#     print("Fail Please Try Again")





# 17 program UserName or Password
# userName = "hello"
# passWord = 123
# User = input("Enter the userName: ")
# if userName == User:
#     PassWo = int(input("Enter the password: "))
#     if passWord == PassWo:
#         print("You are scuccesfully loging!")
#     else:
#         print("Wrong Password Try Again!")
# else:
#     print("Wrong UserName try Again!")





# 18 program maximum out of four number
a = 303
b = 262
c = 50
d = 2055

if a > b and a > c and a > d:
    print("A is maximum")
elif b > a and b > c and b > d:
    print("B is maximum")
elif c > a and c > b and c > d:
    print("C is maximum")
else:
    print("D is maximum")