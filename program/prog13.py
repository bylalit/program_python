# print("\n")
# customerName = input("Enter your name: ")
# print("***********************************")
# print(f"Welcome to my grocely store {customerName}")
# print("-----------------------------------")
# print("\n")

# print("******************** Items Availabel in Our Store **********************")

# shopItem = {
#     "Toothbrush": 2.3,
#     "Apple": 1.5,
#     "Kiwi": 3.4,
#     "Spinach": 1.2,
#     "Cookie-Jar": 10.0,
#     "Water-Bottle": 2.0,
#     "Juice": 4.0,
#     "Milk": 3.0,
#     "Coffee": 7.0,
#     "Chips": 2.0,
#     "Eggs": 4.5
# }

# for x,y in shopItem.items():
#     print(x, ":", y)
#     # print(x.upper(), ":", y)
    
# print("****************************")
# start = (input("Do you wish to proceed with shopping(yes/no)? "))
# order = {}

# while start == "yes":
#     itemName = input("Add item: ")
    
#     if itemName in shopItem:
#         itemQunt = int(input("Add quantity: "))
#         order[itemName] = itemQunt
        
#     else:
#         print("Anable to add item not available!")  
         
#     start = (input("Add more items (yes/no)? "))
#     if start == "yes":
#         print("Choose from below options")

# print("\n")
# print("**************** Bill Summary ****************")
# print("\n")

# print("""Item                 price                 Quantity                 SubTotal""")

# for x,y in order.items():
#     if x in shopItem: 
#         print(f"""{x}                 {shopItem[x]}                 {y}                 {shopItem[x] * y}""")





student = {
    "Lait" :{
        "Maths": 85,
        "Science": 90,
        "English": 78
        },
    "Rohan" :{
        "Maths": 90,
        "Science": 85,
        "English": 92
        },
    "Aman" :{
        "Maths": 78,
        "Science": 92,
        "English": 85
    }
}

for i in student:
    print(i)
    for x,y in student[i].items():
        print(f"{x} : {y}")