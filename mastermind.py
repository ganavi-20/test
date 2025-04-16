import random

def generate_code():
    return [str(random.randint(1, 6)) for _ in range(4)]

def get_feedback(code, guess):
    exact = sum(c == g for c, g in zip(code, guess))
    code_copy = code[:]
    guess_copy = guess[:]
    
    for i in range(3, -1, -1):
        if code_copy[i] == guess_copy[i]:
            del code_copy[i]
            del guess_copy[i]
    
    partial = 0
    for g in guess_copy:
        if g in code_copy:
            partial += 1
            code_copy.remove(g)
    
    return exact, partial
def play_game():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is between 1 and 6.")
    print("You get feedback as:")
    print("- Exact: Correct number in the correct position")
    print("- Partial: Correct number but in the wrong position\n")

    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: ").strip()

        if len(guess) != 4 or not all(ch in "123456" for ch in guess):
            print("Invalid input. Enter exactly 4 digits between 1 and 6.\n")
            continue

        guess_list = list(guess)
        exact, partial = get_feedback(secret_code, guess_list)

        print(f"Exact: {exact}, Partial: {partial}\n")

        if exact == 4:
            print("🎉 Congratulations! You cracked the code!")
            break
    else:
        print(f"😢 Out of attempts! The code was: {''.join(secret_code)}")

play_game()
