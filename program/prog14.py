import math

# 1. program

# a = 10
# b = 20

# a = a + b
# b = a -b
# a = a - b
# print(a)
# print(b)

# temp = b
# b = a
# a = temp
# print(a)
# print(b)


# 2. program

# print("Enter the two complex number in form of a + bj:")
# n1 = complex(input("Enter the first: "))
# n2 = complex(input("Enter the secound: "))

# print("sum = ", n1 + n2)


# 4. progarm

# y = range(1, 30, 2)
# for i in  y:
#     print(i, end=" ")


# 5.program

# a = 10
# b = 20
# list = [1,2,3,4,5,6]

# if a in list:
#     print("A is avalable in list.")
# else:
#     print("A is not avalable in list.")
# print("\n")   
# if b not in list:
#     print("B is not list in present.")
# else:
#     print("B is present in list.")
# print("\n")
# a = 2

# if a in list:
#     print("A is present in list.")
# else:
#     print("A is not present in list.")



# 6. program

# a = 20
# b = 20

# if a is b:
#     print("A and B have same identity.")
# else:
#     print("A and B have not same identity.")

# print("\n")
# if id(a) == id(b):
#     print("A and B have same identity.")
# else:
#     print("A and B have not same identity.")
    
# print("\n")
# b = 30
# if a is b:
#     print("A and B have  same identity.")
# else:
#     print("A and B have not same identity.")
    
# if a is not b:
#     print("A and B have not same identity.")
# else:
#     print("A and B have same identity.")



# 7. program

#  10 + 8 -9 * 2 - (10 * 2)
# x = input("Enter any expression: ")
# print(eval(x))


# 9. program

# 1. pi * r * r
# 2. s = (a + b + c) / 2
    # area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# 3. pi * r * r * h
# 4. simple_interest = (principal * rate * time) / 100

# choice = 0
# while choice == 0:
#     print("1. Find area of circle.")
#     print("2. Find area of trinagle.")
#     print("3. Area of square of rectangle.")
#     print("4. Find simple interest.")
#     print("5. Exit.")
    
#     option = int(input("Enter your choice: "))
    
#     if option == 1:
#         print("a")
#     elif option == 2:
#         a = float(input("Enter the first side of the triangle: "))
#         b = float(input("Enter the second side of the triangle: "))
#         c = float(input("Enter the third side of the triangle: "))

#         s = (a + b + c) / 2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         print(f"The area of the triangle is: {area}")

#     elif option == 3:
#         side = float(input("Enter the side length of the square: "))
#         square_area = side * side
#         print(f"The area of the square is: {square_area}")

#         length = float(input("Enter the length of the rectangle: "))
#         width = float(input("Enter the width of the rectangle: "))
#         rectangle_area = length * width
#         print(f"The area of the rectangle is: {rectangle_area}")
        
#     elif option == 4:
#         principal = float(input("Enter the principal amount: "))
#         rate = float(input("Enter the rate of interest: "))
#         time = float(input("Enter the time in years: "))
        
#         simple_interest = (principal * rate * time) / 100
#         print(f"The simple interest is: {simple_interest}")
        
#     elif option == 5:
#         choice = 1



# 10. program

# num = int(input("Enter a number: "))
# assert num >= 0, "Only positive numbers accepted."
# print("Your Enterd: ", num)


# 11. program

# def search(list, n):
#     for i in list:
#         # print(i)
#         if i == n:
#             return True
        
        
# list = ["sachin", 23 , 12, "python", 90]

# n = "python"

# if search(list, n):
#     print("Found")
# else:
#     print("Not found")



# 12. program 

# cm = int(input("Enter the length in cm: "))
# if cm < 0:
#     print("Invalid Entery")
# else:
#     print(cm/2.54, "inches")










# 1 program

# a = 10
# b = 20

# a = a+b
# b = a-b
# a = a-b

# print(a)
# print(b)



# 2. program

# n1 = 2 + 3j
# n2 = 3 + 2j

# sum = n1 + n2

# print(sum)


# 3. progaram

# nub = 6
# arr = bytes(nub)
# print(arr)

# arr = bytes(3)
# print(arr)

# lis = [12,10,4,5]
# arr = bytes(lis)
# print(arr)


# 4. program

# y = range(1,30, 2)

# for i in y:
#     print(i, end=" ")


# 5. progaram

# a = 10
# b = 20
# lis = [2,4,5,6,7,9]

# if a in lis:
#     print("a is avalable in list")
# else:
#     print("A is not avalable in the list.")
    
# if b not in lis:
#     print("B is not in list.")
# else:
#     print("B is  avalable in list.")   
    
# a = 2
# if a in lis:
#     print("A is avalable in list.")
# else:
#     print("A is not avalable in list.")




#  6. program

# a = 20
# b = 20

# if a is b:
#     print("Same as its")
# else:
#     print("Not same")
    
    
# if id(a) == id(b):
#     print("same to same")
# else:
#     print("Not same")
    
    
# b = 30

# if a is b :
#     print("same")
# else:
#     print("not same")
    

# if a is not b:
#     print("not same")
# else:
#     print('same')


#  7. program


# x = input("Enter the value: ")
# print(eval(x))


# 8. program

# a = int(input("Enter the starting number: "))
# b = int(input("Enter the ending number: "))

# even_num = 0
# odd_num = 0

# for i in range(a, b+1):
#     if i % 2 == 0:
#         even_num += i
#     else:
#         odd_num += i
        
# print("The sum of even number: ",  even_num)
# print("The sum of odd number: ",  odd_num)




# 9. program

# 1. pi * r * r
# 2. s = (a + b + c) / 2
    # area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# 3. pi * r * r * h
# 4. simple_interest = (principal * rate * time) / 100

# choice = 0
# while choice == 0:
#     print("1. Find area of circle.")
#     print("2. Find area of trinagle.")
#     print("3. Area of square of rectangle.")
#     print("4. Find simple interest.")
#     print("5. Exit.")
    
#     option = int(input("Enter your choice: "))
    
#     if option == 1:
#         print("a")
#     elif option == 2:
#         a = float(input("Enter the first side of the triangle: "))
#         b = float(input("Enter the second side of the triangle: "))
#         c = float(input("Enter the third side of the triangle: "))

#         s = (a + b + c) / 2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         print(f"The area of the triangle is: {area}")

#     elif option == 3:
#         side = float(input("Enter the side length of the square: "))
#         square_area = side * side
#         print(f"The area of the square is: {square_area}")

#         length = float(input("Enter the length of the rectangle: "))
#         width = float(input("Enter the width of the rectangle: "))
#         rectangle_area = length * width
#         print(f"The area of the rectangle is: {rectangle_area}")
        
#     elif option == 4:
#         principal = float(input("Enter the principal amount: "))
#         rate = float(input("Enter the rate of interest: "))
#         time = float(input("Enter the time in years: "))
        
#         simple_interest = (principal * rate * time) / 100
#         print(f"The simple interest is: {simple_interest}")
        
#     elif option == 5:
#         choice = 1



# 10. program

# num = int(input("Enter the number: "))
# assert num >= 0, "Only positiv enumber accpted."
# print("Your number: ", num)



#  11. program

# def search(list, n):
#     for i in list:
#         # print(list[i])
#         if i == n:
#             return True
        
#     # list = [2, 5, 8, 12, 16, 23
#     # n = 12
# list = [2, 5, 8, 12, 16, 23]
# n = 1
# # print(search(list, n))
# if  search(list, n):
#     print("Element is present in the list")
# else:
#     print("not found!")



# # 12. program

# cm = int(input("Enter length in cm: "))
# if cm < 0:
#     print("Invalid input")
# else:
#     print(cm/ 2.54, "inches")
    




# Unit 2 practical example

# 1. program

x = [12, 23, 45, 78, 12, 32, 43]
print("Original Array")
print(x)
y = []
y[:] = x
print("New Array")
print(y)