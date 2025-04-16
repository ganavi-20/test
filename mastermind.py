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
