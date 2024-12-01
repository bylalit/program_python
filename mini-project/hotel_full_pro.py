


while True:
    print("----------------------------------------------------")
    print("--------------------Admin Side ---------------------")
    print("----------------------------------------------------")
    
    started = {}
    main = {}
    desart = {}
    
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
            modify = input("""----------------------------------------------------
                                Modify the Started Menu
                    1. Add Item for Press 1
                    2. Delete Item for Press 2
                    3. Delete Item for Perticuler name so Press 3
                    4. Add Item for Press 4""")
            
            if modify == 1:
                wantDish = int(input("How many item add for secound time in started ?:  "))
                
                for i in range(addDish):
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
                