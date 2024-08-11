# total = 1000
# count = 0

# while total >= 1:
#     amt = int(input("Enter the shopping amount of the product: "))
#     total -= amt
    
#     print("Your final amount of the total is: ", total)
#     count += 1
    
# print("Think you for shopping of the shop")
# print(count)



# count = 0
# for i in range(1, 11):
#     if i <= 9:
#         print(i, end= " + ")
#     else:
#         print(i, end= " ")
#     count += i
    
# print("=",count)


user = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
for i in range(user, end):
    if i % 2 == 0:
        print(i, end=" ")
