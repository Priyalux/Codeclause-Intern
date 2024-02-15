import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0

    while True:
        # Get user input for a guess
        user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
