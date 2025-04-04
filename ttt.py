def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
 def check_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False
def play_game():
    board = [[" "]*3 for _ in range(3)]  # Initialize empty board
    player = "X"  # Start with player X
    
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter row and column (0-2) separated by space: ").split())
        
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Cell already taken, try again.")
            continue
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):  # Check if board is full
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"  # Switch player

if __name__ == "__main__":
    play_game()
