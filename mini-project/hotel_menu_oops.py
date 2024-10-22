# Hotem menu program using oops

class HotelMenu:
    started = {}
    main = {}
    deseart = {}
    
    
    def __init__(self, name):
        print("--------------------------HOTEL MENU ADMIN SIDE PENAL--------------------------")
        self.name = name
        
    def add_item(self, item, price, choice):
        if choice == 1:
            if item in self.started:
                print("Item already exists")
            else:
                self.started[item] = price
                print("Item added successfully")
        elif choice == 2:
            if item in self.main:
                print("Item already exists")
            else:
                self.main[item] = price
                print("Item added successfully")
        elif choice == 3:
            if item in self.deseart:
                print("Item already exists")
            else:
                self.deseart[item] = price
                print("Item added successfully")
    
    def delete_item(self):
        HotelMenu.started.popitem()
        print("Item deleted successfully")
            
    def del_index_item(self, item):
        if item in self.started:
            HotelMenu.started.pop(item)
            print("Item deleted successfully")
        else:
            print("Item not found")
    
menu = HotelMenu("Lalit")

print("""Select One Choice
                   1. Press 1 for Started
                   2. Press 2 for Main
                   3. Press 3 for Deserted
                   Enter Your Choice: """)
print()
option = int(input("Enter Your Choice: "))
print()

if option == 1:
    print("Started Menu")
    how = int(input("How many item you want to add? "))
    while how > 0:
        name = input("Enter the name of item: ")
        price = int(input("Enter the price of item: "))
        menu.add_item(name, price)
        how -= 1
    print(menu.started)
    
    
    modify = 1
    
    while modify == 1:
        print()
        update = input("Do you want to update the startes menu so press y or n: ")
        print()
        
        if update == "y":
            print("""Modify Your Startes Menu:
                   1. Press 1 for Insert Item
                   2. Press 2 for Delete Item
                   3. Press 3 for Delete Item by index
                   4. Press 4 for Exit in Modify""")
            
            choice = int(input("Enter Your choice for Modify: "))
            
            if choice == 1:
                how = int(input("How many item you want to add? "))
                while how > 0:
                    name = input("Enter the name of item: ")
                    price = int(input("Enter the price of item: "))
                    menu.add_item(name, price)
                    how -= 1
                print()
                print(menu.started)
                
            elif choice == 2:
                menu.delete_item()
                print()
                print(menu.started)
                
            elif choice == 3:
                how = int(input("How many item you want to delete? "))
                while how > 0:
                    name = input("Enter the name of item you want to delete: ")
                    menu.del_index_item(name)
                    how -= 1
                print()
                print(menu.started)
                
            elif choice == 4:
                modify = 0
                print("Order is placed")

        elif update == "n":
            modify = 0
            print("Thanking For Visit Us Again :)")


elif option == 2:
    print("Main Menu ")