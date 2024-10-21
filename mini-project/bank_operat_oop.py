# Bank operating using oop

class Bank:
    bankname = "Indian Express Bank"
    branch = "Kolkata, India"
    
    # create account
    def __init__(self, username,pan,address):
        self.username = username
        self.pan = pan
        self.address = address
        print(f'Hello {self.username} cong! your account created successfully!')
        
username = input('Enter Your Name: ')
pan = input("Enter PAN card number: ")
address = input("Enter Your Address: ")

b = Bank(username, pan, address)