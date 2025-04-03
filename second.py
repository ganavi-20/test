import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congrats! You guessed the number in {attempts} attempts.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        guess_number()

guess_number()
