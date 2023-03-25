
#==================================================================================================================
#===================================================LOVAC==========================================================
#==================================================================================================================
from board import *
def find_DLG_bishop_moves(board, row, col):
    moves = []

    testlista = board.get_board1()
    #gore
    for r in range(1, 12+1):
        if r != row:
            for c in range(1, 12+1):
                if c+col<=12 and col-c>=1:
                    if testlista[row+r][col+c] is None:
                        moves.append([row+r,col+c])
                    else:
                        # black vraca boolean znaci true:
                        if testlista[row+r][col+c]["black"] != testlista[row][col]["black"] and testlista[row+r][col+c]["type"] != "C":
                            moves.append([row+r,col+c])

                    if testlista[row + r][col - c] is None:
                        moves.append([row + r, col - c])
                    else:
                        # black vraca boolean znaci true:
                        if testlista[row + r][col - c]["black"] != testlista[row][col]["black"] and testlista[row + r][col - c]["type"] != "C":
                            moves.append([row + r, col - c])

    #dole
    for r in range(1, row+1):
        if r != row:
            for c in range(1, 12+1):
                if c+col<=12 and col-c>=1:
                    if testlista[row+r][col+c] is None:
                        moves.append([row+r,col+c])
                    else:
                        if testlista[row + r][col - c]["black"] != testlista[row][col]["black"] and testlista[row + r][col - c]["type"] != "C":
                            moves.append([row+r,col+c])

                    if board[row+r][col-c] is None:
                        moves.append([row+r,col-c])
                    else:
                        if testlista[row + r][col - c]["black"] != testlista[row][col]["black"] and testlista[row + r][col - c]["type"] != "C":
                            moves.append([row+r,col+c])

    return moves


#==================================================================================================================
#==================================================PIJAN===========================================================
#==================================================================================================================

def find_pawn_moves(board, row, col):
    moves = []
    testlista = board.get_board1()

    if testlista[row][col]['black'] != True :
        if row == 2:
            if testlista[row + 2][col + 2] == None:
                moves.append((row + 2, col + 2))
            if testlista[row + 2][col - 2] == None:
                moves.append((row + 2, col - 2))
            if testlista[row + 1][col + 1] == None:
                moves.append((row + 1, col + 1))
            if testlista[row + 1][col - 1] == None:
                moves.append((row + 1, col - 1))

            if testlista[row + 1][col + 1] is not None:
                if testlista[row + 1][col + 1]['black']:
                    moves.append((row + 1, col - 1))

            if board[row + 1][col] is None:
                moves.append((row + 1, col))

            # todo provjeri je li cigla ispred
        else:
            if board[row + 1][col + 1] == None:
                moves.append((row + 1, col + 1))
            if board[row + 1][col - 1] == None:
                moves.append((row + 1, col - 1))
            if board[row + 1][col] != None:
                moves.append((row + 1, col))


    else:
        if row == 11:
            if board[row - 2][col - 2] == None:
                moves.append((row - 2, col - 2))
            if board[row - 2][col + 2] == None:
                moves.append((row - 2, col + 2))
            if board[row - 1][col - 1] == None:
                moves.append((row - 1, col - 1))
            if board[row - 1][col + 1] == None:
                moves.append((row - 1, col + 1))
            if board[row - 1][col] != None:
                moves.append((row - 1, col))
        else:
            if board[row - 1][col - 1] == None:
                moves.append((row - 1, col - 1))
            if board[row - 1][col + 1] == None:
                moves.append((row - 1, col + 1))
            if board[row - 1][col] != None:
                moves.append((row - 1, col))

    return moves

#==================================================================================================================
#===============================================LUDI KONJ==========================================================
#==================================================================================================================

def find_knight_moves(board, row, col):
    moves = []
    testlista = board.get_board1()

    # Check all possible L-shape moves
    l_moves = [(3,1), (1,3), (-1,3), (-3,1), (-3,-1), (-1,-3), (1,-3), (3,-1)]
    for move in l_moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 1 <= new_row <= 12 and 1 <= new_col <= 12 and (testlista[new_row][new_col] is not None or testlista[new_row][new_col]['black'] != testlista[row][col]['black']) and testlista[new_row][new_col]["type"] != "C":
            moves.append([new_row, new_col])

    return moves

#==================================================================================================================
#==================================================TOPG============================================================
#==================================================================================================================

def find_rook_moves(board, row, col, color):
    moves = []

    # Check horizontal and vertical moves
    for i in range(row+1, 12):
        if board[i][col] == None:
            moves.append((i, col))
        elif board[i][col].color != color:
            #i nije cigla
            moves.append((i, col))
            break
        else:
            break

    for i in range(row-1, -1, -1):
        if board[i][col] == None:
            moves.append((i, col))
        elif board[i][col].color != color:
            #i nije cigla
            moves.append((i, col))
            break
        else:
            break

    for j in range(col+1, 12):
        if board[row][j] == None:
            moves.append((row, j))
        elif board[row][j].color != color:
            #i nije cigla
            moves.append((row, j))
            break
        else:
            break

    for j in range(col-1, -1, -1):
        if board[row][j] == None:
            moves.append((row, j))
        elif board[row][j].color != color:
            #i nije cigla
            moves.append((row, j))
            break
        else:
            break

    return moves


# ==================================================================================================================
# ==================================================KRALJ===========================================================
# ==================================================================================================================


def find_king_moves(board, row, col, color):
    moves = []

    # Check all adjacent squares
    for c in range(-1, 1):
        for r in range(-1, 1):
            if c != 0 and r != 0:
                if board[row + r][col + c] == None or (board[row + r][col + c].color != color and  # nije cigla):
                                                       moves.append((row + r, col + c))
            return moves


# ==================================================================================================================
# ================================================KRALJICA==========================================================
# ==================================================================================================================

def find_queen_moves(board, row, col, color):
    moves = []

    # Check diagonal moves________________________________
    # gore desno
    i = 1
    while i > 0 and i < 13 and board[row + i][col + i] == None:
        i += 1
        if row + i >= 12 or col + i >= 12:
            break
    if board[row + i][col + i].color() == color  # or is cigla
        moves.append(row + i - 1, col + i - 1)
    else:
        moves.append(row + i, col + i)

    # dole livo
    i = 1
    while i > 0 and i < 13 and board[row - i][col - i] == None:
        i += 1
        if row - i <= 0 or col - i <= 0:
            break
    if board[row - i][col - i].color() == color  # or is cigla
        moves.append(row - i + 1, col - i + 1)
    else:
        moves.append(row - i, col - i)

    # dole desno
    i = 1
    while i > 0 and i < 13 and board[row - i][col + i] == None:
        i += 1
        if row - i <= 0 or col + i >= 12:
            break
    if board[row - i][col + i].color() == color  # or is cigla
        moves.append(row - i + 1, col + i + 1)
    else:
        moves.append(row - i, col + i)

    # gore livo
    i = 1
    while i > 0 and i < 13 and board[row + i][col - i] == None:
        i += 1
        if row + i >= 12 or col - i <= 0:
            break
    if board[row + i][col - i].color() == color  # or is cigla
        moves.append(row + i - 1, col - i - 1)
    else:
        moves.append(row + i, col - i)

    # Check horizontal and vertical moves_________________________________________
    # gore
    i = 1
    while board[row + i][col] == None and row + i >= 12:
        i += 1
    if board[row + i][col].color() == color  # or is cigla
        moves.append(row + i - 1, col - 1)
    else:
        moves.append(row + i, col)
    # dole
    i = 1
    while board[row - i][col] == None and row - i <= 0:
        i += 1
    if board[row + i][col - i].color() == color  # or is cigla
        moves.append(row + i - 1, col - i - 1)
    else:
        moves.append(row + i, col)

    # livo
    i = 1
    while board[row][col - 1] == None and col - i <= 0:
        i += 1
    if board[row][col - i].color() == color  # or is cigla
        moves.append(row, col - i - 1)
    else:
        moves.append(row, col - i)

    # desno
    i = 1
    while board[row][col + 1] == None and col + i <= 12:
        i += 1
    if board[row][col + i].color() == color  # or is cigla
        moves.append(row, col + i - 1)
    else:
        moves.append(row, col + i)

    return moves


# ==================================================================================================================
# ==================================================SNIPER==========================================================
# ==================================================================================================================

def find_sniper_moves(board, row, col, color):
    moves = []

    # Check all adjacent squares
    for c in range(-2, 2):
        for r in range(-2, 2):
            if c != 0 and r != 0:
                if board[row + r][col + c] == None or (board[row + r][col + c].color != color): #todo and nije cigla
                       moves.append([row + r, col + c])

    return moves


# ==================================================================================================================
# =================================================KAMIKAZA=========================================================
# ==================================================================================================================

def find_kamikaza_moves(board, row, col, color):
    moves = []

    l_moves = [(2, 2), (2, -2), (-2, 2), (-2, -2)]

    # Check all adjacent squares
    for move in l_moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 1 <= new_row <= 12 and 1 <= new_col <= 12 and (
                board[new_row][new_col] == None or board[new_row][new_col].color != color):  # i nije cigla
            moves.append((new_row, new_col))

    return moves