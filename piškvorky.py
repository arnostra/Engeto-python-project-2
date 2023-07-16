'''
"""
piškvorky.py: druhý projekt do Engeto Online Python Akademie

author: Arnošt Razima
email: razima.ar@seznam.cz
discord: Arnošt R. #3251
"""
import ...
'''

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        row = ' '.join(board[i])
        print(f"{i} {row}")

def get_move(player):
    move = input(f"Player {player}, enter your move (row, column): ")
    move = move.strip().split(",")
    move = tuple(map(int, move))
    return move

def is_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    if (board[2][0] == player and board[1][1] == player and board[0][2] == player):
        return True
    return False

def play_game():
    board = [["-" for i in range(3)] for j in range(3)]
    player = "X"
    print_board(board)
    while True:
        move = get_move(player)
        if (board[move[0]][move[1]] != "-"):
            print("Invalid move, try again.")
            continue
        board[move[0]][move[1]] = player
        print_board(board)
        if (is_win(board, player)):
            print(f"Player {player} wins!")
            return
        if (all(all(row != "-" for row in board[i]) for i in range(3))):
            print("Tie game!")
            return
        player = "O" if player == "X" else "X"

play_game()
