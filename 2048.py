import random
import os

def init_board():
    board = [[0]*4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 4 if random.random() > 0.9 else 2

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("+-----"*4 + "+")
        print("".join(f"|{str(num).center(5) if num else '     '}" for num in row) + "|")
    print("+-----"*4 + "+")

def merge(row):
    new = [i for i in row if i != 0]
    for i in range(len(new)-1):
        if new[i] == new[i+1]:
            new[i] *= 2
            new[i+1] = 0
    return [i for i in new if i != 0] + [0]*(4-len([i for i in new if i != 0]))
def move_left(board):
    return [merge(row) for row in board]

def move_right(board):
    return [merge(row[::-1])[::-1] for row in board]

def move_up(board):
    rotated = list(zip(*board))
    moved = move_left([list(row) for row in rotated])
    return [list(row) for row in zip(*moved)]

def move_down(board):
    rotated = list(zip(*board))
    moved = move_right([list(row) for row in rotated])
    return [list(row) for row in zip(*moved)]

def can_move(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if j < 3 and board[i][j] == board[i][j+1]:
                return True
            if i < 3 and board[i][j] == board[i+1][j]:
                return True
    return False

def play():
    board = init_board()
    while True:
        print_board(board)
        move = input("Use WASD to move (w=up, s=down, a=left, d=right): ").lower()

        if move not in 'wasd':
            continue
