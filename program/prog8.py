play = 1

while play == 1:
    started = []
    main = []
    desart = []
    
    prograss = 1
    
    while prograss == 1:
        
    
        choice = int(input("""
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        1. You want add your menu in a started then press 1
        2. You want add your menu in a main then press 2
        3. You want add your menu in a desart then press 3
        choice press : """))
        
        if choice == 1:
            print("started")
            num = int(input("How many desicess add in the started: "))
            
            for i in  range(num):
                name = input("Enter your desicess name: ").upper()
                started.append(name)
                
            process = 1
            
            while process == 1:
                print("\n", started)
                getInput =  int(input("""
    ---------------------------------------------------------
        1. Do you want to add more desicess in the started press 1 or 
        2. Do you want to add index for particular in the started press 2
        3. Do you want to delete desicess in the started press 3
        4. Do you want to delete index for particular in the started press 4
        5. Do you want to exit press 5
        choice press : """))
                
                if  getInput == 1:
                    vale = int(input("How many dicesess add: "))
                    for i in range(vale):
                        dishName = input("Enter the desicess name: ").upper()
                        started.append(dishName)
                    print(started)
                elif getInput == 2:
                    index = int(input("Enter the index number of add desicess: "))
                    name = input("Enter the name of desicess: ").upper()
                    started.insert(index, name)
                    print(started)
                elif getInput == 3:
                    started.pop()
                    print(started)
                elif getInput == 4:
                    index = int(input("Enter the index number of delete desicess: "))
                    started.pop(index)
                    print(started)
                elif getInput == 5:
                    process = 0

                if  getInput == 5:
                    process = 0
                    print("You are exict for the started menu")
                else:
                    process = int(input("Do you want to continu for press 1: "))
    
    
        elif choice == 2:
            print("main")
            num = int(input("How many desicess store in the main: "))
            
            for i in  range(num):
                name = input("Enter your desicess name: ").upper()
                main.append(name)
                
            process = 1
            
            while process == 1:
                print("\n", main)
                getInput =  int(input("""
    ---------------------------------------------------------
        1. Do you want to add more desicess in the main press 1 or 
        2. Do you want to add index for particular in the main press 2
        3. Do you want to delete desicess in the main press 3
        4. Do you want to delete index for particular in the main press 4
        5. Do you want to exit press 5
        choice press : """))
                
                if  getInput == 1:
                    vale = int(input("How many main add: "))
                    for i in range(vale):
                        dishName = input("Enter the desicess name: ").upper()
                        main.append(dishName)
                    print(main)
                elif getInput == 2:
                    index = int(input("Enter the index number of add desicess: "))
                    name = input("Enter the name of desicess: ").upper()
                    main.insert(index, name)
                    print(main)
                elif getInput == 3:
                    main.pop()
                    print(main)
                elif getInput == 4:
                    index = int(input("Enter the index number of delete desicess: "))
                    main.pop(index)
                    print(main)
                elif getInput == 5:
                    process = 0

                process = int(input("Do you want to continu for press 1: "))
                
                
        elif choice == 3:
            print("desart")
            num = int(input("How many desicess store in the desart: "))
            
            for i in  range(num):
                name = input("Enter your desicess name: ").upper()
                desart.append(name)
                
            process = 1
            
            while process == 1:
                print("\n", desart)
                getInput =  int(input("""
    ---------------------------------------------------------
        1. Do you want to add more desicess in the desart press 1 or 
        2. Do you want to add index for particular in the desart press 2
        3. Do you want to delete desicess in the desart press 3
        4. Do you want to delete index for particular in the desart press 4
        5. Do you want to exit press 5
        choice press : """))
                
                if  getInput == 1:
                    vale = int(input("How many main add: "))
                    for i in range(vale):
                        dishName = input("Enter the desicess name: ").upper()
                        desart.append(dishName)
                    print(desart)
                elif getInput == 2:
                    index = int(input("Enter the index number of add desicess: "))
                    name = input("Enter the name of desicess: ").upper()
                    desart.insert(index, name)
                    print(desart)
                elif getInput == 3:
                    desart.pop()
                    print(desart)
                elif getInput == 4:
                    index = int(input("Enter the index number of delete desicess: "))
                    desart.pop(index)
                    print(desart)
                elif getInput == 5:
                    process = 0

                process = int(input("Do you want to continu for press 1: "))
        
        prograss = int(input("Do you want to again add data so press 1: "))





    data = 1
    while data == 1:
        print("\n")
        print("---------------------------------------------------------")
        orderStarted = []
        orderMain = []
        orderDesart = []
        print("""Which want to order for the menu
                        1. started for press 1
                        2. main for press 2
                        3. desart for press 3""")

        choice = int(input("Enter your choice: "))


        if choice == 1:
            print(started)
            wantDish = int(input("How many dish want to order: "))
            count = 0
            while wantDish > count:
                val = input("Enter the name of dishess: ").upper()
                if val in started:
                    orderStarted.append(val)
                    count += 1
                else:
                    print("Not avalible this dish")
            print(orderStarted)
            print("\n")
            

            print("""Can You update your Order than:
                    1. add dish for press 1
                    2. delete dish for press 2""")

            update = int(input("Enter the choice for update order: "))
            
            if update == 1:
                val = input("Enter the dish name for add: ").upper()
                if val in started:
                    orderStarted.append(val)
                else:
                    print("Not avalible this dish")
                print(orderStarted)
            elif update == 2:
                val = input("Enter the dish name for delete: ").upper()
                if val in orderStarted:
                    orderStarted.remove(val)
                print(orderStarted)
        
        elif choice == 2:
            print(main)
            wantDish = int(input("How many dish want to order: "))
            count = 0
            while wantDish > count:
                val = input("Enter the name of dishess: ").upper()
                if val in started:
                    orderMain.append(val)
                    count += 1
                else:
                    print("Not avalible this dish")
            print(orderMain)
            print("\n")

            print("""Can You update your Order than:
                    1. add dish for press 1
                    2. delete dish for press 2""")

            update = int(input("Enter the choice for update order: "))
            
            if update == 1:
                val = input("Enter the dish name for add: ").upper()
                if val in main:
                    orderMain.append(val)
                else:
                    print("Not avalible this dish")
                print(orderMain)
            elif update == 2:
                val = input("Enter the dish name for delete: ").upper()
                if val in orderMain:
                    orderMain.remove(val)
                print(orderMain)
                
                
        
        elif choice == 3:
            print(desart)
            wantDish = int(input("How many dish want to order: "))
            count = 0
            while wantDish > count:
                val = input("Enter the name of dishess: ").upper()
                if val in started:
                    orderDesart.append(val)
                    count += 1
                else:
                    print("Not avalible this dish")
            print(orderDesart)
            print("\n")

            print("""Can You update your Order than:
                    1. add dish for press 1
                    2. delete dish for press 2""")

            update = int(input("Enter the choice for update order: "))
            
            if update == 1:
                val = input("Enter the dish name for add: ").upper()
                if val in desart:
                    orderDesart.append(val)
                else:
                    print("Not avalible this dish")
                print(orderDesart)
            elif update == 2:
                val = input("Enter the dish name for delete: ").upper()
                if val in orderDesart:
                    orderDesart.remove(val)
                print(orderDesart)

        data = int(input("Do you want to order more? press 1 for yes, 2 for no: "))
        
        
    play = int(input("Do you want to play again press 1: "))
