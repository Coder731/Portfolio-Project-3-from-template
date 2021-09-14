# https://www.includehelp.com/python/row-numbers-in-a-matrix.aspx
import numpy as np

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


player_symbol = 'O'


def is_game_over():
    # Check for 3 in a row horizontally
    # Check for 3 in a column vertically
    # Check for 3 in a line diagonally
    # Check if there no space left

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

    for row_i in row_throughput:
        for col_j in col_throughput:
            print("row_i: ", row_i)
            print("col_j: ", col_j)
            print("len(row_i): ", len(row_i))
            print("len(col_j): ", len(col_j))
            # do something with row_i
            # print((board[row_i][col_j]))
            print(board[0][0])


combo()


# https://www.includehelp.com/python/row-numbers-in-a-matrix.aspx

# Use of np.array() to define a matrix
# V = np.array([[1,2,3],[2,3,5],[3,6,8],[323,623,823]])
# print("--The Matrix-- \n",V)

# number of rows
# num = len(V)

# print("Number of rows in the Given Matrix : ", num)


def print_board():
    for row in board:
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
