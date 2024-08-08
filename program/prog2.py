# wantValue = int(input("Enter the value: "))
# i = 1
# value = []
# while i <= wantValue:
#     name = input("Enter the menu name: ")
#     value.append(name)
#     i+=1
# print(value)


paly = 1 

while paly == 1:    
    print("You want to add data to presss 1 \nYou want to delete data to presss 2 \nYou want to delete data from the perticular Index to presss 3")
    choise = int(input("Enter the valid number : "))
    
    if choise == 1:
        store = input("Enter the add data item name: ")
        def add(x):
            value.append(x)
            print(value)
        add(store)
    elif choise == 2:
        def remove():
            value.pop()
            print(value)
        remove()
    elif choise == 3:
        store = int(input("Enter the index of you want to delete: "))
        def remove(x):
            value.pop(x)
            print(value)
        remove(store)
    else:
        print("Please enter the valid choice")
    paly = int(input("If you want to add, delete process again than press 1 othrwise 0 press: "))