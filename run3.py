# Credit Comment:
# https://youtu.be/BHh654_7Cmw?t=562
# Step 0 Build Board

# Add board to present choice
board_to_present_choice1 = [1, 2, 3]
board_to_present_choice2 = [4, 5, 6]
board_to_present_choice3 = [7, 8, 9]

print(board_to_present_choice1[0]),
      board_to_present_choice1[1],
      board_to_present_choice1[2])
print(board_to_present_choice2[0],
      board_to_present_choice2[1],
      board_to_present_choice2[2])
print(board_to_present_choice3[0],
      board_to_present_choice3[1],
      board_to_present_choice3[2])

new_board = {"a": "[ ]", "b": "[ ]", "c": "[ ]", "d": "[ ]",
             "e": "[ ]", "f": "[ ]", "g": "[ ]", "h": "[ ]", "i": "[ ]"}

print(new_board["a"], new_board["b"], new_board["c"])
print(new_board["d"], new_board["e"], new_board["f"])
print(new_board["g"], new_board["h"], new_board["i"])

move = input("Please enter a number from 1 to 9: ")

if (move == 1):
    new_board["a"] = "[ X ]"

# set X for move of 1 equal to X in 1 position
