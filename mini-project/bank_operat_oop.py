# # Bank operating using oop

# class Bank:
#     bankname = "Indian Express Bank"
#     branch = "Kolkata, India"
    
#     # create account
#     def __init__(self, username,pan,address):
#         self.username = username
#         self.pan = pan
#         self.address = address
#         self.balance = 0.0
#         print(f'Hello {self.username} cong! your account created successfully!')


#     # deposit
#     def deposite(self, amount):
#         self.balance = self.balance + amount
#         print(f'{amount} deposited successfully!')


#     # withdraw
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Low Balance, Can Not WithDrow")
#         else:
#             self.balance -= amount
#             print(f'{amount} withdrawn successfully!')
    
    
#     # ministatement
#     def ministatement(self):
#         print(f'Your account balance is {self.balance}')
    
    
    

# print()
# print(f'Welcome to {Bank.bankname}, {Bank.branch}')      
# print()

# username = input('Enter Your Name: ')
# pan = input("Enter PAN card number: ")
# address = input("Enter Your Address: ")

# b = Bank(username, pan, address)


# while True:
#     print()
#     print('Please choose from below options: ')
#     print('1. Deposite\n2. Withdraw\n3. Ministatement\n4. Exit')
    
#     # option = int(input('Enter your choice: '))
#     option = input('Enter your choice: ')
#     print()
    
#     if option.isdigit():
#         option = int(option)
#     else:
#         print('Please enter a valid option')
#         continue
    
#     if option == 1:
#         amount = float(input("Enter Deposite amount: "))
#         b.deposite(amount)
    
#     elif option == 2:
#         amount = float(input("Enter Withdraw amount: "))
#         b.withdraw(amount)    
    
#     elif option == 3:
#         b.ministatement()
    
#     elif option == 4:
#         print(f'Thanking for using {Bank.bankname} ...')
#         break
    
#     else:
#         print("Please selected a valid option")




















class Bank:
    bankName = "Indian Express Bank"
    brance = "Kotak Mumbai, India"
    
    def __init__(self, username, pan, address):
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0
        print(f'Hello {self.username} cong! your account created successfully!')
        
    # deposite
    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f'Your Balance is {self.balance} deposite successfully!')
        
    # withdraw
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Low Balance, Can Not WithDrow")
            
    # miniStatement
    def ministatement(self):
        print(f'Your Balance is {self.balance}')
        
print()
print(f"Welcome to {Bank.bankName}, {Bank.brance}")        
print()
        
username = input("Enter Your Name: ")
pan = input("Enter Your PAN card number: ")
address = input("Enter Your Address: ")

b = Bank(username, pan, address)

while True:
    print()
    print("Please choose from below options: ")
    print("1. Deposite\n2. Withdraw\n3. Ministatement\n4. Exit")
    
    option = input("Enter your choice: ")
    
    print()
    
    if option.isdigit():
        option = int(option)
    else:
        print("Please enter a valid option")
        continue
        
    if option == 1:
        amount = float(input("Enter Deposite amount: "))
        b.deposite(amount)
    elif option == 2:
        amount = float(input("Enter Withdraw amount: "))
        b.withdraw(amount)
    elif option == 3:
        b.ministatement()
    elif option == 4:
        print(f"Thanking for using {Bank.bankName} ...")
        break
    else:
        print("Please selected a valid option")
    
