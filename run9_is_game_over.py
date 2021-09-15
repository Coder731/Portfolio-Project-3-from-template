# https://www.includehelp.com/python/row-numbers-in-a-matrix.aspx
import numpy as np

# https://www.askpython.com/python-modules/pandas/update-the-value-of-a-row-dataframe
import pandas as pd

# https://datatofish.com/pandas-version-installed/
print(pd.__version__)

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


player_symbol = 'O'


def is_game_over():
    # Check for 3 in a row horizontally
    for x in range(3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2]:
            return True

    # Check for 3 in a column vertically
    for y in range(3):
        if board[0][y] == board[1][y] and board[1][y] == board[2][y]:
            return True

    # Check for 3 in a line diagonally
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
            (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return True

    # Check if there no space left
    is_all_filled = True
    for x in range(3):
        for y in range(3):
            if board(x)(y) == ' ':
                is_all_filled = False
                break
        if not is_all_filled:
            break

    if is_all_filled:
        return True
    # https://stackoverflow.com/questions/53101229/how-to-iterate-through-a-matrix-column-in-python
    # for row_i in board:
    #   for col_j in enumerate(row_i):  # enumerate -> (index,value) tuple
    #       # print('test')
    #   #    # print(board[row_i][col_j])
    #   #    ##  for board[row], board[col] in board:
    #   #    # if board[row_i][col_j] != ' ':
    #   #        # row_i = row_i + 1
    #   #        # col_j = col_j + 1
    #       return False  # Allows game to continue
    return False


def combo():
    # Returns
    # TEST: No. of rows in board:  3
    # TEST: No. of rows in board:  3

    # row counter
    row_throughput = np.array(board)
    row_count = len(row_throughput)
    print("TEST: No. of rows in board: ", row_count)
    # col counter
    col_throughput = np.array(board)
    col_count = len(col_throughput)
    print("TEST: No. of rows in board: ", col_count)

    loop_count = 0

    for row_i in row_throughput:
        for col_j in col_throughput:
            if board[r][c] == " ":
                print("spaces available")
                break
            loop_count += 1
            print('loop_count: ', loop_count)
            print("row_i: ", row_i)
            print("col_j: ", col_j)
            print("len(row_i): ", len(row_i))
            print("len(col_j): ", len(col_j))

            # ilok()
            # https://www.askpython.com/python-modules/pandas/update-the-value-of-a-row-dataframe
            if row_i == row_throughput and col_j == col_throughput and \
                    board.iloc[[r],[c]] != " ":
                # board.iloc[[r],[c]][r][c] != " ":
                print("no more spaces available, game over")
                break

            # above print returns:

            # row_i:  [' ' ' ' ' ']
            # col_j:  [' ' ' ' ' ']
            # len(row_i):  3
            # len(col_j):  3

            # do something with row_i
            # print((board[row_i][col_j]))

            for row_var_2 in board:
                # a
                print("row_var_2: ", row_var_2)
            print(board[0][0])


combo()


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
