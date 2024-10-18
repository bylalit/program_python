import sys

class Bank(object):
    def  __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        
    def deposite(self, amount):
        self.balance += amount
        return  self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Low Balance, Can Not WithDrow")
        else:
            self.balance -= amount
            return self.balance
        
name = input("Enter Name: ")

b = Bank(name)

while True:
    print("d/D -deposite, w/W -withdrawal, e/E -exits")
    choice = input("Enter Your Choice: ")
    
    if choice == "e" or choice == "E":
        print("Thanks for using our Bank")
        sys.exit()
        
    amount = float(input("Enter amount: "))
    if  choice == "d" or choice == "D":
        print("Balance after deposite: ", b.deposite(amount))
    elif  choice == "w" or choice == "W":
        print("Balance after withdrawal: ", b.withdraw(amount))


