# Play Game Program 

cardBal = 10000
play = 1

while play == 1:
    print("Enter the play game zone")
    choice = int(input("1. Car racing : 200 \n2. cycling racing : 350 \n3. jumping boll : 420 \nEnter the choice: "))

    if choice == 1:
        if cardBal >= 200:
            print("Welcome the car racing")
            cardBal -= 200
        else:
            print("Ensaficiant balance")
    elif choice == 2:
        if cardBal >= 350:
            print("Welcome the cycling racing")
            cardBal -= 350
        else:
            print("Ensaficiant balance")
    elif choice == 3:
        if cardBal >= 420:
            print("Welcome the jumping boll")
            cardBal -= 350
        else:
            print("Ensaficiant balance")
    else:
        print("Please valid choice number and correct number enter")
    
    print("Your corrent balance is: ", cardBal)
    play = int(input("Do you want to again play? yes for press 1 and exict for press 0: "))
    
    if cardBal <= 420:
        print("Do u want to balance of your cardBal ? then press 1: ")
        bal = int(input("Enter the choice you card balance : "))
        
        if bal == 1:
            valu = int(input("Enter the value you want to store the card bal : "))
            cardBal += valu
            print("Your card balance is: ", cardBal)
        else:
            print("Thank you for play the game")