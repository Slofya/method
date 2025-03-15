from engine import run_game
from games import game1, game2


def main():
    print("Select a game:")
    print("1. Find the greatest common divisor")
    print("2. Find the missing number in the progression")
    choice = input("Enter the number of the game: ")

    if choice == "1":
        run_game(game1)
    elif choice == "2":
        run_game(game2)
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()