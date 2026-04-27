from dice_game import play_dice

def game_menu():
    while True:
        print("\n===== DICE GAME MENU =====")
        print("1. Play Dice Game")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            play_dice()
        elif choice == 2:
            print("Thank you for playing")
            break
        else:
            print("Invalid choice")

game_menu()