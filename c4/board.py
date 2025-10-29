def create_board():
    board = []

    for i in range(6):
        row = []
        for j in range(7):
            row.append("_")
        board.append(row)

    return  board

def column_is_full(board):
    for i in range(6):
        if "_" in board[i]:
            return True
    return False

# def drop_disc():

def legal_moves(board):
    legal = []

    for i in range(7):
        if board[0][i] == "_":
            legal.append(i + 1)
    return legal

def render(board):
    str_board = ""

    for i in range(7):
        if i == 6:
            str_board += "\n"
        str_board += "|"
        str_board += " "

        for j in range(7):
            if i == 6:
                str_board += str(j)
            else:
                str_board += board[i][j]
            str_board += " "
            str_board += "|"
            str_board += " "


        str_board += "\n"
    return str_board



















