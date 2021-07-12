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


def get_input():
    x = int(input("X: "))
    y = int(input("Y: "))
    print(f"You selected: ({x},{y})")
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
    return False


def check_filled(board):
    return False


if __name__ == "__main__":
    game_board = create_board()
    print_board(game_board)
    x, y = get_input()
    game_board[2][2] = "X"
    print(check_valid(0, 0, game_board))
    print(check_valid(1, 2, game_board))
    print(check_valid(0, 4, game_board))
    print(check_valid(5, 1, game_board))

    while not check_winner and not check_filled:
        exit()
