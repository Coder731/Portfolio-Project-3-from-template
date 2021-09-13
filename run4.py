board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def take_user_name_input():
    name = input("Enter Name ")
    if not name:
        return take_user_name_input()
    else:
        return name


def init_game():
    name = take_user_name_input()
    print("Name entered is : ", name)


init_game()
