import random

words = ["python", "banana", "guitar", "rocket", "castle"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  

print("🎯 Welcome to the Word Guessing Game!")
print("Guess the word one letter at a time.")
