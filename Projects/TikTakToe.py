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
    x = 0
    y = 0
    valid_input = False
    while not valid_input:
        try:
            x = int(input("X: "))
            y = int(input("Y: "))
            valid_input = True
        except Exception as inst:
            print("Invalid inputs. Please enter numbers")
    return x, y


def check_valid(x, y, board):
    # if x >= 0 and x < rows
    # if y >= 0 and y < cols
    # if both satisfied, then you have valid cords
    # if pos is X or O, then false, else true

    # Check values on board
    if not (0 <= x < len(board[0]) and 0 <= y < len(board)):
        print(f"Values {x}, {y} are out of bounds. Try again.")
        return False
    # Check values are empty
    if board[x][y] == "X" or board[x][y] == "O":
        print(f"Values {x},{y} are already taken. Try again.")
        return False
    # Return True Otherwise
    return True


def place_mark(player, board):
    print(f"{player}'s turn")
    x, y = get_input()
    while not check_valid(x, y, board):
        x, y = get_input()
    board[x][y] = player
    print_board(board)


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

def start_two_player_game():
    game_board = create_board()
    print_board(game_board)
    turn_count = 0
    while not check_winner(game_board) and not check_filled(game_board):
        if turn_count % 2 == 0:
            place_mark("X", game_board)
        else:
            place_mark("O", game_board)
        turn_count += 1

    # Check Winner
    if check_winner(game_board):
        print(f"Game Winner: {check_winner(game_board)}")
    elif check_filled(game_board):
        print("Game Tied")
    else:
        "Something Happened"

if __name__ == "__main__":
    ans = input("Hello please type the corresponding number for your preferred option:\n1). Two Player\n"
                "2). Player vs AI\n3). Exit\n--> ")
    if ans == "1":
        start_two_player_game()
    elif ans == "2":
        print("Placeholder")
    else:
        print("Goodbye")

    # game_board = create_board()
    # print_board(game_board)
    # turn_count = 0
    # while not check_winner(game_board) and not check_filled(game_board):
    #     if turn_count % 2 == 0:
    #         place_mark("X", game_board)
    #     else:
    #         place_mark("O", game_board)
    #     turn_count += 1
    #
    # # Check Winner
    # if check_winner(game_board):
    #     print(f"Game Winner: {check_winner(game_board)}")
    # elif check_filled(game_board):
    #     print("Game Tied")
    # else:
    #     "Something Happened"
#  exit()

# Fix Check Valid switch x and y
# Build AI
# Pulling Down Other Project via Git
