
#==================================================================================================================
#===================================================LOVAC==========================================================
#==================================================================================================================

def find_DLG_bishop_moves(board, row, col):
    moves = []

    #gore
    for r in range(1, 12+1):
        if r != row:
            for c in range(1, 12+1):
                if c+col<=12 and col-c>=1:
                    if board[row+r][col+c] == None:
                        moves.append(row+r,col+c)
                    #else:
                        #if board[row+r][col+c].color() = suprotna boja:
                            #i nije cigla
                            #moves.append(row+r,col+c)
                    if board[row+r][col-c] == None:
                        moves.append(row+r,col-c)
                    #else:
                        #if board[row+r][col+c].color() = suprotna boja:

                            #i nije cigla

                            #moves.append(row+r,col+c)
                
    #dole
    for r in range(1, row):
        if r != row:
            for c in range(1, 12):
                if c+col<=12 and col-c>=1:
                    if board[row+r][col+c] == None:
                        moves.append(row+r,col+c)
                    #else:
                        #if board[row+r][col+c].color() = suprotna boja:
                        #i nije cigla
                            #moves.append(row+r,col+c)
                    if board[row+r][col-c] == None:
                        moves.append(row+r,col-c)
                    #else:
                        #if board[row+r][col+c].color() = suprotna boja:
                        #i nije cigla
                            #moves.append(row+r,col+c)
    
    return moves


#==================================================================================================================
#==================================================PIJAN===========================================================
#==================================================================================================================

def find_pawn_moves(board, row, col, color):
    moves = []

    if color == 'w':
        if row == 1:
            if board[row + 2][col + 2] == None:
                moves.append((row + 2, col + 2))
            if board[row + 2][col - 2] == None:
                moves.append((row + 2, col - 2))
            if board[row + 1][col + 1] == None:
                moves.append((row + 1, col + 1))
            if board[row + 1][col - 1] == None:
                moves.append((row + 1, col - 1))
            # PROVJERA JEL MOJA BOJA ISPRED
            # if board[row + 1][col] != None:
            #     moves.append((row + 1, col))

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

def find_knight_moves(board, row, col, color):
    moves = []
    
    # Check all possible L-shape moves
    l_moves = [(3,1), (1,3), (-1,3), (-3,1), (-3,-1), (-1,-3), (1,-3), (3,-1)]
    for move in l_moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 1 <= new_row <= 12 and 1 <= new_col <= 12 and (board[new_row][new_col] == None or board[new_row][new_col].color != color):
            #i nije cigla
            moves.append((new_row, new_col))
    
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

#==================================================================================================================
#==================================================KRALJ===========================================================
#==================================================================================================================


def find_king_moves(board, row, col, color):
    moves = []
    
    # Check all adjacent squares
    for i in range(max(0, row-1), min(row+2, 12)):
        for j in range(max(0, col-1), min(col+2, 12)):
            if i == row and j == col:
                continue
            if board[i][j] == None or board[i][j].color != color:
                moves.append((i, j))
    
    return moves


#==================================================================================================================
#================================================KRALJICA==========================================================
#==================================================================================================================

def find_queen_moves(board, row, col, color):
    moves = []
    
    # Check diagonal moves
    #gore desno
    i=1 
    while i > 0 and i < 13 and board[row+i][col+i] != None:
        i +=1
        if row + i >= 12 or col + i >= 12:
            break
    if board[row+i][col+i].color()==color #or is cigla
        moves.append(row+i-1,col+i-1)
    else:
        moves.append(row+i,col+i)
    
    #dole livo
    i=1
    while i > 0 and i < 13 and board[row-i][col-i] != None:
        i +=1
        if row - i <= 0 or col - i <= 0:
            break
    if board[row-i][col-i].color()==color #or is cigla
        moves.append(row-i+1,col-i+1)
    else:
        moves.append(row-i,col-i)

    #dole desno
    i=1
    while i > 0 and i < 13 and board[row-i][col+i] != None:
        i +=1
        if row - i <= 0 or col + i >= 12:
            break
    if board[row-i][col+i].color()==color #or is cigla
        moves.append(row-i+1,col+i+1)
    else:
        moves.append(row-i,col+i)

    #gore livo
    i=1 
    while i > 0 and i < 13 and board[row+i][col-i] != None:
        i +=1
        if row + i >= 12 or col - i <= 0:
            break
    if board[row+i][col-i].color()==color #or is cigla
        moves.append(row+i-1,col-i-1)
    else:
        moves.append(row+i,col-i)

    
    # Check horizontal and vertical moves
    #gore
    for i in range(row+1, 12):
        if board[i][col] == None:
            moves.append((i, col))
        elif board[i][col].color != color:
            moves.append((i, col))
            break
        else:
            break
    
    for i in range(row-1, -1, -1):
        if board[i][col] == None:
            moves.append((i, col))
        elif board[i][col].color != color:
            moves.append((i, col))
            break
        else:
            break
            
    for j in range(col+1, 12):
        if board[row][j] == None:
            moves.append((row, j))
        elif board[row][j].color != color:
            moves.append((row, j))
            break
        else:
            break
    
    for j in range(col-1, -1, -1):
        if board[row][j] == None:
            moves.append((row, j))
        elif board[row][j].color != color:
            moves.append((row, j))
            break
        else:
            break
    
    return moves

#==================================================================================================================
#==================================================SNIPER==========================================================
#==================================================================================================================

#==================================================================================================================
#=================================================KAMIKAZA=========================================================
#==================================================================================================================