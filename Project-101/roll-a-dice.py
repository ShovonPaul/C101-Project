import random

while True:
    response = input("Do you want to roll the dice? (y/n): ")
    
    if response.lower() != "y":
        print("Thanks for playing! Goodbye.")
        break

    dice_number = random.randint(1, 6)

    print(" ------- ")
    print("|       |")
    print("|   {}   |".format(dice_number))
    print("|       |")
    print(" ------- ")

    response = input("Roll the dice again? (y/n): ")

    if response.lower() != "y":
        print("Thanks for playing! Goodbye.")
        break
