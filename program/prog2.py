wantValue = int(input("Enter the value: "))
i = 1
value = []
while i <= wantValue:
    name = input("Enter the menu name: ")
    value.append(name)
    i+=1
print(value)

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