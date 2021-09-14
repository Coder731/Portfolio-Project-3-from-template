board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

r = 0
c = 0

# index()
for r in board.index([r]):
    for c in board.index([r][c]):
        if board.index([r][c]) != " ":
            print(f"board[{r}][{c}] is occupied.")
        elif board.index([r][c]) == " ":
            print(f"board[{r}][{c}] is first empty cell.")
            print("game continues")
            break
