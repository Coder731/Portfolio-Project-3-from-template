# board is a list of lists
# each row is a nested list
# each cell is blank space
board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def take_user_choice():
    move = int(input('Enter number between 1-9'))
    if not move or move < 1 or move > 9:
        print('Invalid input')
        return take_user_choice()


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
