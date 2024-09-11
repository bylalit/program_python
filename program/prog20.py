# # ATM program in python

# print("\nWelcome to ABC Bank\n")
# print("Insert your ATM card\n")

# password = 1234
# balance = 10000
# pin = int(input("Enter your Four digit card pin number: "))


# choice = 0
# if pin == password:
    
#     while choice != 4:
#         print("\n\n****Menu****\n1. ** Balance\n2. ** Deposit\n3. ** Withdraw\n4. ** Cancel")
    
#         choice = int(input("\nEnter your choice: "))
    
#         if choice == 1:
#             print("Your corrent balance is: Rs.", balance)
            
#         elif choice == 2:
#             dep = int(input("Enter  the amount you want to deposit: Rs."))
#             balance += dep
#             print("Your deposit aount is:  Rs.", dep)
#             print("Your new balance is: Rs.", balance)
            
#         elif choice == 3:
#             wid = int(input("Enter  the amount you want to withdraw: Rs."))
#             balance -= wid
#             print("Your withdraw aount is:  Rs.", wid)
#             print("Your new balance is: Rs.", balance)
            
#         elif choice == 4:
#             print("Thank you for using our ATM service")
        
#         else:
#             print("Invalid choice, please try again!")


#     print("---Repl Closed---")
    
# else:
#     print("Incorrect password try again!")