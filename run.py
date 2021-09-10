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

values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
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
