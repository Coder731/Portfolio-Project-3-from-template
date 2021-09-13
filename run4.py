# board is a list of lists
# each row is a nested list
# each cell is blank space
board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


# function takes username and checks that
# name was not left blank
# by pressing enter without
# entering a name:
def take_user_name_input():
    name = input("Enter Name ")
    if not name:
        return take_user_name_input()
    else:
        return name


# initialise game by calling function to take
# and return user name then print result
def init_game():
    name = take_user_name_input()
    print("Name entered is : ", name)


# call function to initialise game
init_game()
