import random

# Number Guessing Game
# Has difficulty levels, limited attempts, replay option, and better hints

def choose_difficulty():
    # shows the menu and gets a valid choice from the user
    print("\nSelect Difficulty:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 500, 5
        else:
            print("Invalid choice, pick 1, 2 or 3.")


def get_hint(guess, target, max_range):
    # gives a more useful hint than just "too high/too low"
    # based on how far off the guess is compared to the range
    diff = abs(guess - target)
    closeness = diff / max_range  # how far off, as a % of the range

    if guess > target:
        if closeness > 0.3:
            return "Very High"
        elif closeness > 0.1:
            return "Slightly High"
        else:
            return "Very Close, but still high"
    else:
        if closeness > 0.3:
            return "Very Low"
        elif closeness > 0.1:
            return "Slightly Low"
        else:
            return "Very Close, but still low"


def play_round(low, high, attempts):
    # runs a single game with the given range and attempt count
    target = random.randint(low, high)
    attempts_left = attempts

    print(f"\nI'm thinking of a number between {low} and {high}. You have {attempts} attempts.")

    while attempts_left > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if guess == target:
            print(f"You got it! The number was {target}.")
            return True

        attempts_left -= 1
        hint = get_hint(guess, target, high - low)
        print(hint)
        print(f"Attempts Remaining: {attempts_left}")

    print(f"Out of attempts! The number was {target}.")
    return False


def number_guessing_game():
    # main loop that handles replay
    while True:
        low, high, attempts = choose_difficulty()
        play_round(low, high, attempts)

        play_again = input("\nPlay Again? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    number_guessing_game()