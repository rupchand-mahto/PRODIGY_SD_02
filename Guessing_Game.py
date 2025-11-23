import random

def guessing_game():
    print("🎮 Welcome to the Guessing Game!")
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1–100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < number:
            print("📉 Too low! Try again.")
        elif guess > number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break

# Start the game
guessing_game()
