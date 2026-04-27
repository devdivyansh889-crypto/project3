import random
from utils import max_dice

def play_dice():
    print("\nRolling Dice...")

    user_roll = random.randint(1, max_dice)
    computer_roll = random.randint(1, max_dice)

    print("You rolled:", user_roll)
    print("Computer rolled:", computer_roll)

    if user_roll > computer_roll:
        print("You Win ")
    elif user_roll < computer_roll:
        print("Computer Wins ")
    else:
        print("Match Draw")