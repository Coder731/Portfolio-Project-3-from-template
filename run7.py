import numpy as np

import pandas as pd

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

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

    loop_count = 0

    """
    for row_i in row_throughput:
        for col_j in col_throughput:
            if board[row_i][col_j] == " ":
                print("spaces available")
                break
            loop_count += 1
            print('loop_count: ', loop_count)
            print("row_i: ", row_i)
            print("col_j: ", col_j)
            print("len(row_i): ", len(row_i))
            print("len(col_j): ", len(col_j))

            # index()
            # for r, c in board.index([r][c]):
            # if board.index([r][c]) == " ":
    """

    # index()
    for r in board.index([r]):
        for c in board.index([r][c]):
            if board.index([r][c]) != " ":
                print(f"board[{r}][{c}] is occupied.")
            elif board.index([r][c]) == " ":
                print(f"board[{r}][{c}] is first empty cell.")
                print("game continues")
                break

            # ilok()
            # https://www.askpython.com/python-modules/pandas/update-the-value-of-a-row-dataframe
            # if row_i == row_throughput and col_j == col_throughput and \
                # board.iloc[[r], [c]] == value_to_set_to:
            # board  [rows, cols] -> set to this

                # board.iloc[[r],[c]] != " ":
                # board.iloc[[r],[c]][r][c] != " ":
                # print("no more spaces available, game over")
                # break

            # above print returns:

            # row_i:  [' ' ' ' ' ']
            # col_j:  [' ' ' ' ' ']
            # len(row_i):  3
            # len(col_j):  3

            # do something with row_i

            for row_var_2 in board:
                # a
                print("row_var_2: ", row_var_2)
            print(board[0][0])


combo()
