# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# testing terminal input
# Credit Comment
# https://techeplanet.com/python-read-input-from-terminal-stdin/
name = input("Enter Name ")
print("Name entered is : ", name)
print(type(name))

# Add code to check if integer is used, using a while loop:

while True:
    move = input('input number from 1-9 here : ')
    if not move.isdigit():
        # if the user does not enter a digit, continue asking user
        # for move # Note will have to check if in range also [ ]
        continue
    else:
        print("thank you for inputing a digit")
        break

# Credit Comment:
# https://youtu.be/BHh654_7Cmw?t=562
# Step 0 Build Board
board1 = [1, 2, 3]
board2 = [4, 5, 6]
board3 = [7, 8, 9]

board = ["[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]"]

a = {x: print(board[x], board[(x+1)], board[(x+2)]) for x in range(0, 8, 3)}

# Step 1 Check User Selection:
print("User enter your move (1-9):")
move2 = input("enter choice")
print(board1)
print(board2)
print(board3)

# Add print statement
# https://www.askpython.com/python/examples/tic-tac-toe-using-python


def print_board(values):
    print("\t  {}  |  {}   ".format(values[0], values[1]))


# print_board()


values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
          "f": 6, "g": 7, "h": 8, "i": 9}
# Function to print Tic Tac Toe
# def print_tic_tac_toe(values):
print("\n")
print('\t- - - - - - -')

print("\t| {} | {} | {} |".format(values["a"], values["b"], values["c"]))
print('\t- - + - + - -')

print("\t| {} | {} | {} |".format(values["d"], values["e"], values["f"]))
print('\t- - + - + - -')


print("\t| {} | {} | {} |".format(values["g"], values["h"], values["i"]))
print('\t- - - - - - -')

print("\n")


move = input("Please enter a number from 1 to 9: ")
# format for next step:
# values["a"] = move

if (move == 1):
    values["a"] = "[ X ]"
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["-"]

print("\n")
print('\t- - - - - - -')

print("\t| {} | {} | {} |".format(values["a"], values["b"], values["c"]))
print('\t- - + - + - -')

print("\t| {} | {} | {} |".format(values["d"], values["d"], values["e"]))
print('\t- - + - + - -')


print("\t| {} | {} | {} |".format(values["f"], values["g"], values["h"]))
print('\t- - - - - - -')

print("\n")

# while True:
#     move = input()
#     if not move.isdigit():
#         continue
#     else:


# the input is a digit and we can move on
