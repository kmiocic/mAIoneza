
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

                    if testlista[row+r][col-c] is None:
                        moves.append([row+r,col-c])
                    else:
                        if testlista[row + r][col - c]["black"] != testlista[row][col]["black"] and testlista[row + r][col - c]["type"] != "C":
                            moves.append([row+r,col+c])

    return moves

#=================================================================================================================
def je_li_cigla(board, row, col):
    return board[row][col]["type"] == "C"


#==================================================================================================================
#==================================================PIJAN===========================================================
#==================================================================================================================

def find_pawn_moves(board, row, col):
    moves = []
    testlista = board.get_board1()

    if testlista[row][col]['black'] != True :

        if testlista[row + 1][col] is not None and testlista[row + 1][col]["black"] != testlista[row][col]["black"] and not je_li_cigla(testlista, row+1, col):
                moves.append((row + 1, col))
        if row == 2:
            if testlista[row + 2][col + 2] is None:
                moves.append((row + 2, col + 2))
            if testlista[row + 2][col - 2] is None:
                moves.append((row + 2, col - 2))
            if testlista[row + 1][col + 1] is None:
                moves.append((row + 1, col + 1))
            if testlista[row + 1][col - 1] is None:
                moves.append((row + 1, col - 1))

        else:
            if testlista[row + 1][col + 1] is None:
                moves.append((row + 1, col + 1))
            if testlista[row + 1][col - 1] is None:
                moves.append((row + 1, col - 1))

    else:
        if testlista[row - 1][col] is not None and testlista[row - 1][col]["black"] != testlista[row][col]["black"] and not je_li_cigla(testlista, row-1, col):
                moves.append((row - 1, col))
        if row == 11:
            if testlista[row - 2][col - 2] is None:
                moves.append((row - 2, col - 2))
            if testlista[row - 2][col + 2] is None:
                moves.append((row - 2, col + 2))
            if testlista[row - 1][col - 1] is None:
                moves.append((row - 1, col - 1))
            if testlista[row - 1][col + 1] is None:
                moves.append((row - 1, col + 1))
        else:
            if testlista[row - 1][col - 1] is None:
                moves.append((row - 1, col - 1))
            if testlista[row - 1][col + 1] is None:
                moves.append((row - 1, col + 1))

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
        if testlista[i][col] is None:
            moves.append((i, col))
        elif testlista[i][col]["black"] != testlista[row][col]["black"] and testlista[i][col]["type"] != "C": 
            moves.append((i, col))
            break
        else:
            break

    for i in range(row-1, -1, -1):
        if testlista[i][col] is None:
            moves.append((i, col))
        elif testlista[i][col]["black"] != testlista[row][col]["black"] and testlista[i][col]["type"] != "C":
            moves.append((i, col))
            break
        else:
            break

    for j in range(col+1, 12):
        if testlista[row][j] is None:
            moves.append((row, j))
        elif testlista[row][j]["black"]!= testlista[row][col]["black"] and testlista[row][j]["type"] != "C": 
            moves.append((row, j))
            break
        else:
            break

    for j in range(col-1, -1, -1):
        if testlista[row][j] is None:
            moves.append((row, j))
        elif testlista[row][j]["black"]!= testlista[row][col]["black"] and testlista[row][j]["type"] != "C": 
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
                if testlista[row + r][col + c] is None
                    moves.append((row + r, col + c))
                else:
                    if testlista[row + r][col + c]["black"]!=testlista[row][col]["black"] and testlista[row+r][col+c]["type"] != "C":
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
    while i > 0 and i < 13 and testlista[row + i][col + i] is None:
        i += 1
        if row + i >= 12 or col + i >= 12:
            break
    if testlista[row + i][col + i]["black"] == color  # or is cigla
        moves.append(row + i - 1, col + i - 1)
    else:
        moves.append(row + i, col + i)

    # dole livo
    i = 1
    while i > 0 and i < 13 and testlista[row - i][col - i] is None:
        i += 1
        if row - i <= 0 or col - i <= 0:
            break
    if testlista[row - i][col - i]["black"] == color  # or is cigla
        moves.append(row - i + 1, col - i + 1)
    else:
        moves.append(row - i, col - i)

    # dole desno
    i = 1
    while i > 0 and i < 13 and testlista[row - i][col + i] is None:
        i += 1
        if row - i <= 0 or col + i >= 12:
            break
    if testlista[row - i][col + i]["black"] == color  # or is cigla
        moves.append(row - i + 1, col + i + 1)
    else:
        moves.append(row - i, col + i)

    # gore livo
    i = 1
    while i > 0 and i < 13 and testlista[row + i][col - i] is None:
        i += 1
        if row + i >= 12 or col - i <= 0:
            break
    if testlista[row + i][col - i]["black"] == color  # or is cigla
        moves.append(row + i - 1, col - i - 1)
    else:
        moves.append(row + i, col - i)

    # Check horizontal and vertical moves_________________________________________
    # gore
    i = 1
    while testlista[row + i][col] is None and row + i >= 12:
        i += 1
    if testlista[row + i][col]["black"] == color  # or is cigla
        moves.append(row + i - 1, col - 1)
    else:
        moves.append(row + i, col)
    # dole
    i = 1
    while testlista[row - i][col] is None and row - i <= 0:
        i += 1
    if testlista[row + i][col - i]["black"] == color  # or is cigla
        moves.append(row + i - 1, col - i - 1)
    else:
        moves.append(row + i, col)

    # livo
    i = 1
    while testlista[row][col - 1] is None and col - i <= 0:
        i += 1
    if testlista[row][col - i]["black"] == color  # or is cigla
        moves.append(row, col - i - 1)
    else:
        moves.append(row, col - i)

    # desno
    i = 1
    while testlista[row][col + 1] is None and col + i <= 12:
        i += 1
    if testlista[row][col + i]["black"] == color  # or is cigla
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
                if testlista[row + r][col + c] is None or (testlista[row + r][col + c]["black"] testlista[row][col]["black"]): #todo and nije cigla
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
                testlista[new_row][new_col] is None or testlista[new_row][new_col]["black"] testlista[row][col]["black"]):  # i nije cigla
            moves.append((new_row, new_col))

    return moves