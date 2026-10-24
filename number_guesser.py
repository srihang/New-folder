#This is a number guesser game that will generate a random number from 1-100.
#Then the user will have a chance to try and guess ther number.
#If the user guessing to low or high the system will tell that and the user will have 7 guesses to try and get it right.


import random

MAX_attempts = 7
LOWER_bound = 1
UPPER_bound = 100

def display_rules():
    print("You have to try and guess my number")
    print("I have chosen a number between 1-100")
    print("You have 7 attempts to find my number!")

def play_game():
    secret_number = random.randint(LOWER_bound, UPPER_bound)
    attempts_used = 0

    display_rules()

    while attempts_used < MAX_attempts:
        remaining = MAX_attempts - attempts_used
        print(f"Attempts left: {remaining}")
        raw_guess = input("Enter your guess: ")


        try:
            guess = int(raw_guess)
        except ValueError:
            print("Invalid input! Please enter a whole number.\n")
            continue

        if guess < LOWER_bound or guess > UPPER_bound:
            print(f"Your guess must be between {LOWER_bound} and {UPPER_bound}.\n")
            continue
        
        
        attempts_used += 1

        if guess == secret_number:
            print(f"\nCorrect! You guessed it!")
            return
        elif guess < secret_number:
            print("Too low! Try another number.\n")
        else:
            print("Too high! Try another number.\n")

    print("Game over! You have no more attempts,")
    print(f"The answer was : {secret_number}")

if __name__ == "__main__":
    play_game()