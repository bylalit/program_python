start = 1

while start == 1:
    statred = {}
    main = {}
    desart = {}
    
    again = 1
    
    
    print("\n")
    print("---------------------------------------------------------")
    print("""--------------------- Admin Side -----------------------""")
    print("---------------------------------------------------------")
    
    while again == 1:
        choice = int(input("""
        ---------------------------------------------------------
            1. Started menu add then press 1
            2. Main menu add then press 2
            3. Desart menu add then press 3
            choice one option: """))
        
        if choice == 1:
            dishWant = int(input("How many diceses add in statred: "))
            for i in range(dishWant):
                itemName = input("Enter the item Name: ").upper()
                itemPrice = int(input("Enter the item price: "))
                statred[itemName] = itemPrice
            print(statred)
            
            modify = 1
            
            while modify == 1:
                update = int(input("""
        ---------------------------------------------------------                                   
                    Modify the Started menu:
            1. Add item for press 1
            2. Delete item for press 2
            3. Delete item for particular name so press 3
            4. Exit for press 4
            choice one option: """))
                
                if update == 1:
                    num = int(input("How many item add for secound time in Statred: "))
                    for i in range(num):
                        itemName = input("Enter the item Name: ").upper()
                        itemPrice = int(input("Enter the item price: "))
                        statred[itemName] = itemPrice
                    print(statred)
                elif update == 2:
                    statred.popitem()
                    print(statred)
                elif update == 3:
                    nameItem = input("Which Item you want to delete? please write the Item name: ")
                    statred.pop(nameItem)
                    print(statred)
                elif update == 4:
                    modify = 0
                
                if update == 4:
                    modify = 0
                else:    
                    modify = int(input("Do you again modify started then press 1: "))
            
            
        
        elif choice == 2:
            dishWant = int(input("How many diceses add in main: "))
            for i in range(dishWant):
                itemName = input("Enter the item Name: ").upper()
                itemPrice = int(input("Enter the item price: "))
                main[itemName] = itemPrice
            print(main)
            
            
            modify = 1
            
            while modify == 1:
                update = int(input("""
        ---------------------------------------------------------                                   
                    Modify the Main menu:
            1. Add item for press 1
            2. Delete item for press 2
            3. Delete item for particular name so press 3
            4. Exit for press 4
            choice one option: """))
                
                if update == 1:
                    num = int(input("How many item add for secound time in main: "))
                    for i in range(num):
                        itemName = input("Enter the item Name: ").upper()
                        itemPrice = int(input("Enter the item price: "))
                        main[itemName] = itemPrice
                    print(main)
                elif update == 2:
                    main.popitem()
                    print(main)
                elif update == 3:
                    nameItem = input("Which Item you want to delete? please write the Item name: ")
                    main.pop(nameItem)
                    print(main)
                elif update == 4:
                    modify = 0
                
                if update == 4:
                    modify = 0
                else:    
                    modify = int(input("Do you again modify main then press 1: "))
            
            
        
        elif choice == 3:
            dishWant = int(input("How many diceses add in desart: "))
            for i in range(dishWant):
                itemName = input("Enter the item Name: ").upper()
                itemPrice = int(input("Enter the item price: "))
                desart[itemName] = itemPrice
            print(desart)
            
            
            
            modify = 1
            
            while modify == 1:
                update = int(input("""
        ---------------------------------------------------------                                   
                    Modify the Started menu:
            1. Add item for press 1
            2. Delete item for press 2
            3. Delete item for particular name so press 3
            4. Exit for press 4
            choice one option: """))
                
                if update == 1:
                    num = int(input("How many item add for secound time in desart: "))
                    for i in range(num):
                        itemName = input("Enter the item Name: ").upper()
                        itemPrice = int(input("Enter the item price: "))
                        desart[itemName] = itemPrice
                    print(desart)
                elif update == 2:
                    desart.popitem()
                    print(desart)
                elif update == 3:
                    nameItem = input("Which Item you want to delete? please write the Item name: ")
                    desart.pop(nameItem)
                    print(desart)
                elif update == 4:
                    modify = 0
                
                if update == 4:
                    modify = 0
                else:    
                    modify = int(input("Do you again modify desart then press 1: "))
            
        again = int(input("Do you continue for main menu then press 1: "))
        
    # print("\n")
    # print("Started menu list: ")
    # count = 1
    # for x,y in statred.items():
    #     print(f"{count}. {x}  ----------- Rs.{y} ")
    #     count += 1
    # print("\n")
    
    
    # print("\n")
    # print("Main menu list: ")
    # count = 1
    # for x,y in main.items():
    #     print(f"{count}. {x}  ----------- Rs.{y} ")
    #     count += 1
    
    # print("\n")
    # print("Desart menu list: ")
    # count = 1
    # for x,y in desart.items():
    #     print(f"{count}. {x}  ----------- Rs.{y} ")
    #     count += 1

    
    
    def display(**item):
        count = 1
        for x,y in item.items():
            print(f"{count}. {x}  ----------- Rs.{y} ")
            count += 1
    
    print("\n")
    print("---------------------------------------------------------")      
    print("Started menu list: ")
    display(**statred)
    print("\n")
    print("Main menu list: ")
    display(**main)
    print("\n")
    print("Desart menu list: ")
    display(**desart)
    print("\n")



    print("\n")
    print("----------------------------------------------------------------")
    print("""----------------- User Penal (Customer side) -----------------""")
    print("----------------------------------------------------------------")
    print("\n")

    userStart = 1
    
    startedOrder = {}
    mainOrder = {}
    desrtOrder = {}
    
    while userStart == 1:
        
        userInput = int(input("""
        ---------------------------------------------------------
                Order for menu list:
        1. Started menu order so press 1
        2. Main menu order so press 2
        3. Desart menu order so press 3
        choice one option: """))

        if userInput == 1:
            print("Started menu list: ")
            display(**statred)
            
            item = int(input("How mmany item you want to order: "))
            for i in range(item):
                userOrder = input("Enter your order item name: ").upper()
                if userOrder in statred:
                    startedOrder[userOrder] = statred[userOrder]
                else:
                    print("Not available this dish")
              
            print("Your started order: ", startedOrder)
        
            modify = 1
            
            while modify == 1:

                update = int(input("""
        ---------------------------------------------------------                                   
                    Update the Started menu:
            1. Add item for press 1
            2. Delete item for press 2
            3. Delete item for particular name so press 3
            4. Exit for press 4
            choice one option: """))
                
                
                
                if update == 1:
                    item = int(input("How mmany item you want to add: "))
                    for i in range(item):
                        iName = input("Enter your  order item name: ").upper()
                        if iName in statred:
                            startedOrder[iName] = statred[iName]
                        else:
                            print("Not  available this dish")
                    print("Your started order: ", startedOrder)
                    
                elif  update == 2:
                    item = int(input("How mmany item you want to delete: "))
                    for i in range(item):
                        startedOrder.popitem()
                    print("Your started order: ", startedOrder)
                    
                elif  update == 3:
                    item = int(input("How mmany item you want to delete: "))
                    for i in range(item):
                        iName = input("Enter your  order item name: ").upper()
                        if iName in startedOrder:
                            startedOrder.pop(iName)
                        else:
                            print("Not available this dish")
                    print("Your started order: ", startedOrder)
                            
                elif update == 4:
                    modify = 0
                
            
                if update == 4:
                    modify = 0
                else:
                    modify = int(input("Can you again repeat update for statered order so press 1: "))


                
        elif userInput == 2:
            print("Main menu list: ")
            display(**main)
            
            item = int(input("How many item you want to order: "))
            for i in range(item):
                userOrder = input("Enter your order item name: ").upper()
                if userOrder in main:
                    mainOrder[userOrder] = main[userOrder]
                else:
                    print("Not available this dish")
              
            print("Your main order: ", mainOrder)
        
            modify = 1
            
            while modify == 1:
                update = int(input("""
        ---------------------------------------------------------                                   
                    Update the Started menu:
            1. Add item for press 1
            2. Delete item for press 2
            3. Delete item for particular name so press 3
            4. Exit for press 4
            choice one option: """))
        
                if update == 1:
                    item = int(input("How mmany item you want to add: "))
                    for i in range(item):
                        iName = input("Enter your  order item name: ").upper()
                        if iName in main:
                            mainOrder[iName] = main[iName]
                        else:
                            print("Not  available this dish")
                    print("Your main order: ", mainOrder)
                    
                elif  update == 2:
                    item = int(input("How mmany item you want to delete: "))
                    for i in range(item):
                        mainOrder.popitem()
                    print("Your main order: ", mainOrder)
                    
                elif  update == 3:
                    item = int(input("How mmany item you want to delete: "))
                    for i in range(item):
                        iName = input("Enter your  order item name: ").upper()
                        if iName in mainOrder:
                            mainOrder.pop(iName)
                        else:
                            print("Not available this dish")
                    print("Your main order: ", mainOrder)
                            
                elif update == 4:
                    modify = 0
                
            
                if update == 4:
                    modify = 0
                else:
                    modify = int(input("Can you again repeat update for main order so press 1: "))       
                
                
       
       
        elif userInput == 3:
            print("Desart menu list: ")
            display(**desart)
            
            item = int(input("How many item you want to order: "))
            for i in range(item):
                userOrder = input("Enter your order item name: ").upper()
                if userOrder in desart:
                    desrtOrder[userOrder] = desart[userOrder]
                else:
                    print("Not available this dish")
              
            print("Your desart order: ", desrtOrder)
        
            modify = 1
            
            while modify == 1:
                update = int(input("""
        ---------------------------------------------------------                                   
                    Update the Started menu:
            1. Add item for press 1
            2. Delete item for press 2
            3. Delete item for particular name so press 3
            4. Exit for press 4
            choice one option: """))
        
                if update == 1:
                    item = int(input("How many item you want to add: "))
                    for i in range(item):
                        iName = input("Enter your  order item name: ").upper()
                        if iName in desart:
                            desrtOrder[iName] = desart[iName]
                        else:
                            print("Not  available this dish")
                    print("Your desart order: ", desrtOrder)
                    
                elif  update == 2:
                    item = int(input("How many item you want to delete: "))
                    for i in range(item):
                        desrtOrder.popitem()
                    print("Your desart order: ", desrtOrder)
                    
                elif  update == 3:
                    item = int(input("How many item you want to delete: "))
                    for i in range(item):
                        iName = input("Enter your  order item name: ").upper()
                        if iName in desrtOrder:
                            desrtOrder.pop(iName)
                        else:
                            print("Not available this dish")
                    print("Your desart order: ", desrtOrder)
                            
                elif update == 4:
                    modify = 0
                
            
                if update == 4:
                    modify = 0
                else:
                    modify = int(input("Can you again repeat update for desart order so press 1: "))         
                
        userStart = int(input("Do you want to continue for useradmin page so press 1: "))                  

    start = int(input("Do you continue for All program then press 1: "))

    print("\n")
    print("---------------------------------------------------------")
    print("""----------------Your Order (User side)------------------""")
    print("---------------------------------------------------------")
    
    def userOrderDisplay(**order):
        count = 1
        totalAmount = 0
        for x,y in order.items():
            print(f"{count}. {x} ------------ =>  Rs.{y}")
            totalAmount += y
            count += 1
        print("Your Total Amount is: ", "Rs.",totalAmount)
        
    print("\n")
    print("---------------------------------------------------------")
    print("Your Started order: ")  
    userOrderDisplay(**startedOrder)
    
    print("\n")
    print("---------------------------------------------------------")
    print("Your Main order: ")
    userOrderDisplay(**mainOrder)
    
    print("\n")
    print("---------------------------------------------------------")
    print("Your Desart order: ")  
    userOrderDisplay(**desrtOrder)
    print("\n")
    
    
    print("******************* Thank You For Visit *******************")
    print("\n")
    print("\n")