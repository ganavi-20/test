def choose_word():
    word_list = ["python", "hangman", "programming", "developer", "code", "computer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return " ".join(display)
