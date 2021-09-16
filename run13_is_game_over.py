# Credit Comment
# Many thanks to my mentor, Akshat Garg, for all the help
# on this and previous portfolio projects
# https://github.com/akshatnitd

board = [
        ['O', ' ', ' '],
        ['O', ' ', ' '],
        ['O', ' ', ' ']
    ]


player_symbol = 'O'


def is_game_over():
    # Check for 3 in a column vertically
    for y in range(3):
        print(f"board[0][y]: {board[0][y]}")
        print(f"board[1][y]: {board[1][y]}")
        print(f"board[2][y]: {board[2][y]}")
        print(" 'X' 'O' ")
        if board[0][y] == board[1][y] \
                and board[1][y] == board[2][y] \
                and board[2][y] == ('O'):
            return True

    # https://stackoverflow.com/questions/53101229/how-to-iterate-through-a-matrix-column-in-python


def print_board():
    for row in board:
        print("TEST2: row: ", row)
        print(('---').join(row))


def get_row_col_from_cell(cell):
    col = (int(cell % 3) - 1) % 3
    row = int((cell - 1) / 3)
    return (row, col)


def is_occupied(move):
    global board
    (row, col) = get_row_col_from_cell(move)
    if board[row][col] != ' ':
        return True
    else:
        return False


def take_user_choice():
    move = int(input('Enter number between 1-9: '))
    if not move or move < 1 or move > 9:
        print('Invalid input')
        return take_user_choice()
    elif is_occupied(move):
        print('Already occupied')
        return take_user_choice()
    return move


def change_player_symbol():
    global player_symbol
    if player_symbol == 'X':
        return 'O'
    else:
        return 'X'


def start_game():
    global player_symbol, board
    while not is_game_over():
        print_board()
        player_symbol = change_player_symbol()
        user_choice = take_user_choice()
        (row, col) = get_row_col_from_cell(user_choice)
        board[row][col] = player_symbol


def init_game():
    start_game()


init_game()
