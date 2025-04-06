def choose_word():
    word_list = ["python", "hangman", "programming", "developer", "code", "computer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return " ".join(display)
while attempts > 0 and not guessed_word:
        print(f"\nYou have {attempts} attempts remaining.")
        print(f"Current word: {display_word(word, guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try again.")
            continue
