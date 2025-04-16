import random

words = ["python", "banana", "guitar", "rocket", "castle"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  

print("🎯 Welcome to the Word Guessing Game!")
print("Guess the word one letter at a time.")
while attempts > 0 and "_" in guessed:
    print("\nWord: " + " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct!")
        else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

if "_" not in guessed:
    print(f"\n🎉 You guessed the word: {word}!")
else:
    print(f"\n💀 Game over! The word was: {word}")
