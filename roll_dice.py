import random

def roll_dice():
    min_value = 1
    max_value = 6

    while True:
        print("Rolling the dice...")
        dice_number = random.randint(min_value, max_value)
        print("You rolled a", dice_number)

        roll_again = input("Do you want to roll again? (yes/no): ")
        if roll_again.lower() in ["yes", "y"]:
            continue
        else:
            break

    print("Thanks for playing!")

roll_dice()