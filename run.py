# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Step 0 Build Board
board1 = [1, 2, 3]
board2 = [4, 5, 6]
board3 = [7, 8, 9]

# Step 1 Check User Selection:
print("User enter your move (1-9):")
print(board1)
print(board2)
print(board3)

# Add print statement
# https://www.askpython.com/python/examples/tic-tac-toe-using-python


def print_board(values):
    print("\t  {}  |  {}   ".format(values[0], values[1]))


# print_board()

values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}
# Function to print Tic Tac Toe
# def print_tic_tac_toe(values):
print("\n")
print('\t- - - - - - -')

print("\t| {} | {} | {} |".format(values[0], values[1], values[2]))
print('\t- - + - + - -')

print("\t| {} | {} | {} |".format(values[3], values[4], values[5]))
print('\t- - + - + - -')


print("\t| {} | {} | {} |".format(values[6], values[7], values[8]))
print('\t- - - - - - -')

print("\n")


move = input("Please enter a number from 1 to 9: ")
if (move == 1):
    a = ["X"]
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["-"]
elif (move == 2):
    a = ["-"]
    b = ["X"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["-"]
elif (move == 3):
    a = ["-"]
    b = ["-"]
    c = ["X"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["-"]
elif (move == 4):
    a = ["-"]
    b = ["-"]
    c = ["-"]
    d = ["X"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["-"]

elif (move == 5):
    a = ["-"]
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["X"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["-"]
elif (move == 6):
    a = ["-"]
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["X"]
    g = ["-"]
    h = ["-"]
    i = ["-"]

elif (move == 7):
    a = ["-"]
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["X"]
    h = ["-"]
    i = ["-"]

elif (move == 8):
    a = ["-"]
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["X"]
    i = ["-"]

elif (move == 9):
    a = ["-"]
    b = ["-"]
    c = ["-"]
    d = ["-"]
    e = ["-"]
    f = ["-"]
    g = ["-"]
    h = ["-"]
    i = ["X"]

print("\n")
print('\t- - - - - - -')

print("\t| {} | {} | {} |".format(values[a], values[b], values[c]))
print('\t- - + - + - -')

print("\t| {} | {} | {} |".format(values[d], values[d], values[e]))
print('\t- - + - + - -')


print("\t| {} | {} | {} |".format(values[f], values[g], values[h]))
print('\t- - - - - - -')

print("\n")

while True:
    move = input()
    if not move.isdigit():
        continue
    else:
# the input is a digit and we can move on