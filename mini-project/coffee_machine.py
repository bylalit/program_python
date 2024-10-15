menu ={
    "latte":{
        "ingredients":{
            "water": 500,
            "milk": 200,
            "coffee": 100,
        },
        "cost": 150
    },
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 100
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200
    }
}


profit = 0
resourcess = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


is_on = True
while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resourcess['water']}ml")
        print(f"Water = {resourcess['milk']}ml")
        print(f"Water = {resourcess['coffee']}g")
        print(f"Money = Rs{profit}")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
