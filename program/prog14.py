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
        time = float(input("Enter the time in years: "))
        
        simple_interest = (principal * rate * time) / 100
        print(f"The simple interest is: {simple_interest}")
        
#     elif option == 5:
#         choice = 1