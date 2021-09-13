# board is a list of lists
# each row is a nested list
# each cell is blank space
board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def is_game_over():
    # Check for 3 in a row horizontally
    # Check for 3 in a column vertically
    # Check for 3 in a line diagonally
    return False  # Allows game to continue


def print_board():
    for row in board:  # iterate over board using row counter
        print(('---').join(row))  # use join method with spacer


def get_row_col_from_cell(cell):
    col = (int(cell % 3) - 1) % 3
    row = int((cell - 1) / 3)
    return (row, col)


def is_occupied(move):
    global board  # must use global keyword using board variable in block scope
    (row, col) = get_row_col_from_cell(move)
    if board[row][col] != ' ':  # check if cell is NOT empty
        return True  # if empty cell: is_occupied returns True
    else:
        return False  # if (taken) not empty cell: is_occupied returns False


def take_user_choice():
    move = int(input('Enter number between 1-9'))
    if not move or move < 1 or move > 9:
        print('Invalid input')
        return take_user_choice()
    elif is_occupied(move):
        print('Already occupied')
        return take_user_choice()
    return move


def start_game():
    while not is_game_over():
        print_board()
        user_choice = take_user_choice()
        (row, col) = get_row_col_from_cell(user_choice)


# function takes username and checks that
# name was not left blank
# by pressing enter without
# entering a name:
def take_user_name_input():
    name = input("Enter Name ")
    if not name:  # activated if nothing entered for name
        return take_user_name_input()  # if no name, function re-calls self
    else:  # activated if name IS entered
        return name


# initialise game by calling function to take
# and return user name then print result
def init_game():
    name = take_user_name_input()
    print("Name entered is : ", name)


# call function to initialise game
init_game()