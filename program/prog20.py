#  1. program
import random
target = random.randint(1,100)

while True:
    guss = input("Guess a number between 1 and 100 or Quit(Q): ").upper()

    if guss == "Q":
        break
     
    guss = int(guss)

    if target == guss:
        print("You guessed it! The number was indeed", target)
        break
    elif  target > guss:
        print("Too low!")
    else:
        print("Too high!")

print("-----Game Over------")