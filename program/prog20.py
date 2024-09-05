# ATM program in python

print("Welcome to ABC Bank\n\n")
print("Insert your ATM card")

password = 1234
balance = 10000
pin = int(input("Enter your Four digit pin: "))


choice = 0
if pin == password:
    
    while choice != 4:
        choice = int(input("****Menu****\n1. ** Balance\n2. ** Deposit\n3. ** Withdraw\n4. ** Cancel"))
    
        if choice == 1:
            print("Your corrent balance is: Rs.", balance)
            
        elif choice == 2:
            

    
else:
    print("Incorrect password try again!")