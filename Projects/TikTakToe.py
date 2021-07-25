"""
[
1,2,3
4,5,6
7,8,9
]
"""


def create_board():
    rows, cols = (3, 3)
    board = [(["-"] * cols) for _ in range(rows)]
    return board


def print_board(b):
    for row in b:
        print("")
        for elem in row:
            print(f"{elem} ", end="")
    print()


def get_input():
    x = int(input("X: "))
    y = int(input("Y: "))
    # print(f"You selected: ({x},{y})")
    return x, y


def check_valid(x, y, board):
    # if x >= 0 and x < rows
    # if y >= 0 and y < cols
    # if both satisfied, then you have valid cords
    # if pos is X or O, then false, else true

    # Check values on board
    if not (0 <= x < len(board[0]) and 0 <= y < len(board)):
        return False
    # Check values are empty
    if board[x][y] == "X" or board[x][y] == "O":
        return False
    # Return True Otherwise
    return True


def check_winner(board):
    # Checking Rows for Winner
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "-":
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != "-":
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != "-":
        return board[2][0]
    # Checking Columns for Winner
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != "-":
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != "-":
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != "-":
        return board[0][2]
    # Checking Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    return False


def check_filled(board):
    for row in board:
        for elem in row:
            if elem == "-":
                # Board Not Empty
                return False
    return True


if __name__ == "__main__":
    game_board = create_board()
    print_board(game_board)
    # x, y = get_input()
    # print(check_valid(0, 0, game_board))
    # print(check_valid(1, 2, game_board))
    # print(check_valid(0, 4, game_board))
    # print(check_valid(5, 1, game_board))
    turn_count = 0
    while not check_winner(game_board) and not check_filled(game_board):
        if turn_count % 2 == 0:
            print("X's turn")
            x, y = get_input()
            if check_valid(x, y, game_board):
                game_board[x][y] = "X"
                print_board(game_board)
        else:
            print("O's turn")
            x, y = get_input()
            if check_valid(x, y, game_board):
                game_board[x][y] = "O"
                print_board(game_board)
        turn_count += 1

    # Check Winner
    if check_winner(game_board):
        print(f"Game Winner: {check_winner(game_board)}")
    elif check_filled(game_board):
        print("Game Tied")
    else:
        "Something Happened"

  #  exit()


  # Go again if spot is already taken
  # Input Validation for spot choice (only accepts Ints right now)
  # Build AI
  # Pulling Down Other Project via Git
