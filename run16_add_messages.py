# Credit Comment
# Many thanks to my mentor, Akshat Garg, for all the help
# on this and previous portfolio projects
# https://github.com/akshatnitd

# this file from
# run10_is_game_over.py
# Add
# vertical check conditionals from:
# run14_double_conditions.py

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


player_symbol = 'O'


def is_game_over():
    # Check for 3 in a row horizontally
    for x in range(3):
        if (board[x][0] == board[x][1]
                and board[x][1] == board[x][2]
                and board[x][2] == 'X') or (board[x][0] == board[x][1]
                                            and board[x][1] == board[x][2]
                                            and board[x][2] == 'O'):
            return True

    # Check for 3 in a column vertically
    # Note this goes against the principle of DRY "Do not
    # repeat yourself"
    # However, due to time constraints, current level of understanding
    # of python
    # and the fact that boolean ('X' or 'O')
    # evaluates to X
    # (therefore not testing for 3 'O' in a line)
    # repitition was used as a work around in conditionals:
    for y in range(3):
        if (board[0][y] == board[1][y]
                and board[1][y] == board[2][y]
                and board[2][y] == 'X') or (board[0][y] == board[1][y]
                                            and board[1][y] == board[2][y]
                                            and board[2][y] == 'O'):
            return True

    # Check for 3 in a line diagonally
    if ((board[0][0] == board[1][1]
        and board[1][1] == board[2][2]
            and board[2][2] == 'X') or
            (board[0][2] == board[1][1]
                and board[1][1] == board[2][0]
                and board[2][0] == 'X')) or (board[0][0] == board[1][1]
                                             and board[1][1] == board[2][2]
                                             and board[2][2] == 'O') or \
                                            (board[0][2] == board[1][1]
                                             and board[1][1] == board[2][0]
                                             and board[2][0] == 'O'):
        return True

    # Check if there no space left
    is_all_filled = True
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                is_all_filled = False
                break
        if not is_all_filled:
            break

    if is_all_filled:
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


def take_user_name_input():
    name = input("Enter Name ")
    if not name:
        return take_user_name_input()
    else:
        return name


def init_game():
    name = take_user_name_input()
    print("Name entered is : ", name)
    start_game()


init_game()
