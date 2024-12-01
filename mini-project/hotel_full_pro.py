


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
        addDish = int(input("How many dish add in started: "))
        
        while addDish < 0:
            dish = input("Enter the Dish name: ")
            price = input("Enter the Dish price: ")
            
            started[dish] = price
            