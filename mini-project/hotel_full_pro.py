
start = 1

while start == 1:
    print("----------------------------------------------------")
    print("--------------------Admin Side ---------------------")
    print("----------------------------------------------------")
    
    started = {}
    main = {}
    desart = {}
    
    again = 1
    
    
    while again == 1:
        print("""-------------------------------------------------------------
          1. Started menu add then press 1
          2. Main menu add then press 2
          3. Desart menu add then press 3""")
    
        choice = int(input("Choice One Option: "))
        
        if choice == 1:
            print("WelCome To Started Menu")
            addDish = int(input("How many dish add in started: "))
            
            for i in range(addDish):
                dish = input("Enter the Dish name: ").upper()
                price = input("Enter the Dish price: ")  
                started[dish] = price
            
            print(started)
            
            
            update = 1
            while update == 1:
                modify = int(input("""----------------------------------------------------
                                    Modify the Started Menu
                        1. Add Item for Press 1
                        2. Delete Item for Press 2
                        3. Delete Item for Perticuler name so Press 3
                        4. Add Item for Press 4"""))
                
                if modify == 1:
                    wantDish = int(input("How many item add for secound time in started ?:  "))
                    
                    for i in range(wantDish):
                        dish = input("Enter the Dish name: ").upper()
                        price = input("Enter the Dish price: ")  
                        started[dish] = price
                        
                    print(started)
                    
                elif modify == 2:
                    started.popitem()
                    print(started)
                    
                elif modify == 3:
                    del_want = int(input("How many dish want to delete: "))
                    
                    for i in range(del_want):
                        dish_name = input("Enter your dish name, You want to delete: ").upper()
                        started.pop(dish_name)
                    print(started)
                        
                elif modify ==4:
                    update = 0
                    
                if modify == 4:
                    update = 0
                else:
                    update = int(input("Do you want again modify started so press 1: "))
                    
                    
                    
                    
        elif choice == 2:
            print("WelCome To Main Menu")
            addDish = int(input("How many dish add in main: "))
            
            for i in range(addDish):
                dish = input("Enter the Dish name: ").upper()
                price = input("Enter the Dish price: ")  
                main[dish] = price
            
            print(main)
            
            
            update = 1
            while update == 1:
                modify = int(input("""----------------------------------------------------
                                    Modify the Main Menu
                        1. Add Item for Press 1
                        2. Delete Item for Press 2
                        3. Delete Item for Perticuler name so Press 3
                        4. Add Item for Press 4"""))
                
                if modify == 1:
                    wantDish = int(input("How many item add for secound time in main ?:  "))
                    
                    for i in range(wantDish):
                        dish = input("Enter the Dish name: ").upper()
                        price = input("Enter the Dish price: ")  
                        main[dish] = price
                        
                    print(main)
                    
                elif modify == 2:
                    main.popitem()
                    print(main)
                    
                elif modify == 3:
                    del_want = int(input("How many dish want to delete: "))
                    
                    for i in range(del_want):
                        dish_name = input("Enter your dish name, You want to delete: ").upper()
                        main.pop(dish_name)
                    print(main)
                        
                elif modify ==4:
                    update = 0
                    
                if modify == 4:
                    update = 0
                else:
                    update = int(input("Do you want again modify main menu so press 1: "))
                    
                    
        elif choice == 1:
            print("WelCome To Desert Menu")
            addDish = int(input("How many dish add in deseart: "))
            
            for i in range(addDish):
                dish = input("Enter the Dish name: ").upper()
                price = input("Enter the Dish price: ")  
                desart[dish] = price
            
            print(started)
            
            
            update = 1
            while update == 1:
                modify = int(input("""----------------------------------------------------
                                    Modify the Deserte Menu
                        1. Add Item for Press 1
                        2. Delete Item for Press 2
                        3. Delete Item for Perticuler name so Press 3
                        4. Add Item for Press 4"""))
                
                if modify == 1:
                    wantDish = int(input("How many item add for secound time in started ?:  "))
                    
                    for i in range(wantDish):
                        dish = input("Enter the Dish name: ").upper()
                        price = input("Enter the Dish price: ")  
                        desart[dish] = price
                        
                    print(desart)
                    
                elif modify == 2:
                    desart.popitem()
                    print(desart)
                    
                elif modify == 3:
                    del_want = int(input("How many dish want to delete: "))
                    
                    for i in range(del_want):
                        dish_name = input("Enter your dish name, You want to delete: ").upper()
                        desart.pop(dish_name)
                    print(desart)
                        
                elif modify ==4:
                    update = 0
                    
                if modify == 4:
                    update = 0
                else:
                    update = int(input("Do you want again modify desarte so press 1: "))
                    
        again = int(input("Can You Again Add Data: "))
    
                
    print("\n")
    print("Started Menu List")
    count = 1
    
    for x,y in started.items():
        print(f"{count}. {x}  ----------- Rs.{y} ")
        count += 1
        

    print("\n")
    print("Main Menu List")
    count = 1
    
    for x,y in main.items():
        print(f"{count}. {x}  ----------- Rs.{y} ")
        count += 1
        
        
    print("\n")
    print("Desarte Menu List")
    count = 1
    
    
    for x,y in desart.items():
        print(f"{count}. {x}  ----------- Rs.{y} ")
        count += 1
        