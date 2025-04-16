import random

print("Welcome to the 21 Number Game!")
print("You can say 1 to 3 numbers in a turn. Whoever says 21 loses!")
print("Let's begin!")

current = 0

while current < 21:
    try:
        user_input = input("\nYour turn - enter 1 to 3 numbers separated by space: ").strip().split()
        user_numbers = [int(i) for i in user_input]

        if len(user_numbers) not in [1, 2, 3] or user_numbers[0] != current + 1:
            print("Invalid move. Try again.")
            continue
        if any(user_numbers[i] != user_numbers[i-1] + 1 for i in range(1, len(user_numbers))):
            print("Numbers must be in sequence. Try again.")
            continue

        current = user_numbers[-1]
        print(f"You said: {', '.join(map(str, user_numbers))}")

        if current >= 21:
            print("Oh no! You said 21. You lose!")
            break
comp_count = random.randint(1, 3)
        comp_numbers = list(range(current + 1, current + comp_count + 1))
        current = comp_numbers[-1]
        print(f"Computer says: {', '.join(map(str, comp_numbers))}")

        if current >= 21:
            print("Computer said 21. You win!")
            break
    except ValueError:
        print("Please enter numbers only.")
