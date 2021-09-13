new_board = {"a": "[ ]", "b": "[ ]", "c": "[ ]", "d": "[ ]",
             "e": "[ ]", "f": "[ ]", "g": "[ ]", "h": "[ ]", "i": "[ ]"}

print(new_board["a"], new_board["b"], new_board["c"])
print(new_board["d"], new_board["e"], new_board["f"])
print(new_board["g"], new_board["h"], new_board["i"])

move = input("Please enter a number from 1 to 9: ")

if (move == 1):
    new_board["a"] = "[ X ]"
