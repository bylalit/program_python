# Bank operating using oop

class Bank:
    bankname = "Indian Express Bank"
    branch = "Kolkata, India"
    
    # create account
    def __init__(self, username,pan,address):
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0
        print(f'Hello {self.username} cong! your account created successfully!')


    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f'{amount} deposited successfully!')


print()
print(f'Welcome to {Bank.bankname}, {Bank.branch}')      
print()

username = input('Enter Your Name: ')
pan = input("Enter PAN card number: ")
address = input("Enter Your Address: ")

b = Bank(username, pan, address)


while True:
    print('Please choose from below options: ')
    print('1. Deposite\n2. Withdraw\n3. Ministatement\n4. Exit')
    
    option = int(input(''))
    
    if option == 1:
        amount = float(input("Enter Deposite amount: "))
        b.deposite(amount)