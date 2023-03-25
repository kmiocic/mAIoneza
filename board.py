import json

class Piece:
    def __init__(self, id, type, isblack):
        self.id = id
        self.type = type
        self.isblack = isblack
    
    @classmethod
    def from_dict(cls, dict):
        id = dict["id"]
        type = dict["oznaka"]
        isblack = dict["black"]


        return cls(id, type, isblack)


class Board:
    def __init__(self, board_state1, board_state2, whitePiecesPlacement1, whitePiecesPlacement2,
    blackPijanPlacement1, blackPijanPlacement2, whitePijanPlacement1, whitePijanPlacement2, whiteMoves1, whiteMoves2,
    blackPiecesPlacement1, blackPiecesPlacement2):
        self.board_state1 = board_state1
        self.board_state2 = board_state2
        self.whitePiecesPlacement1 = whitePiecesPlacement1
        self.whitePiecesPlacement2 = whitePiecesPlacement2
        self.blackPijanPlacement1 = blackPijanPlacement1
        self.blackPijanPlacement2 = blackPijanPlacement2
        self.whitePijanPlacement1 = whitePijanPlacement1
        self.whitePijanPlacement2 = whitePijanPlacement2
        self.whiteMoves1 = whiteMoves1
        self.whiteMoves2 = whiteMoves2
        self.blackPiecesPlacement1 = blackPiecesPlacement1
        self.blackPiecesPlacement2 = blackPiecesPlacement2
        

    
    def GwhitePiecesPlacement1(self):
        return self._whitePiecesPlacement1

    
    def GwhitePiecesPlacement2(self):
        return self._whitePiecesPlacement2

    
    def GblackPijanPlacement1(self):
        return self._blackPijanPlacement1

    
    def GblackPijanPlacement2(self):
        return self._blackPijanPlacement2

    
    def GwhitePijanPlacement1(self):
        return self._whitePijanPlacement1

    
    def GwhitePijanPlacement2(self):
        return self._whitePijanPlacement2

    
    def GwhiteMoves1(self):
        return self._whiteMoves1

    
    def GwhiteMoves2(self):
        return self._whiteMoves2

    
    def GblackPiecesPlacement1(self):
        return self._blackPiecesPlacement1

    
    def GblackPiecesPlacement2(self):
        return self._blackPiecesPlacement2


    @classmethod
    def from_json(cls, json_string):
        try:
            data = json.loads(json_string)
            board_state1 = json.loads(data["gameState"])["boardState1"]
            board_state2 = json.loads(data["gameState"])["boardState2"]

            whitePiecesPlacement1 = board_state1['whitePiecesPlacement']
            whitePiecesPlacement2 = board_state2['whitePiecesPlacement']

            blackPiecesPlacement1 = board_state1['blackPiecesPlacement']
            blackPiecesPlacement2 = board_state2['blackPiecesPlacement']

            whitePijanPlacement1 = board_state1['whitePijanPlacement']
            whitePijanPlacement2 = board_state2['whitePijanPlacement']

            blackPijanPlacement1 = board_state1['blackPijanPlacement']
            blackPijanPlacement2 = board_state2['blackPijanPlacement']
            
            whiteMoves1 = board_state1['whiteMoves']
            whiteMoves2 = board_state2['whiteMoves']

            #print(board_state1)
            #print(board_state2)
            #print(whiteMoves1)
            #print(whiteMoves2)
            return cls(board_state1, board_state2, whitePiecesPlacement1, whitePiecesPlacement2,
    blackPijanPlacement1, blackPijanPlacement2, whitePijanPlacement1, whitePijanPlacement2, whiteMoves1, whiteMoves2,
    blackPiecesPlacement1, blackPiecesPlacement2)
        except json.JSONDecodeError as e:
            print(f"Failed to load JSON string: {e}")
            

    # def print_board(self):
    #     for row in self.board_state:
    #         for cell in row:
    #             if cell is None:
    #                 print("-", end=" ")
    #             else:
    #                 print(cell.label, end=" ")
    #         print()
    def print_board(self):
        for row in self.board_state1["board"]:
            print(" ".join([piece["oznaka"] if piece is not None else "-" for piece in row]))
        print("\n")
        for row in self.board_state2["board"]:
            print(" ".join([piece["oznaka"] if piece is not None else "-" for piece in row]))

    
    #ista stvar kao print board samo vrati matricu board 1
    def get_board1(self):
        lista = []
        
        for row in self.board_state1["board"]:
            lista +=[[piece for piece in row]]
        return lista

    #board 2 matrica
    def get_board2(self):
        lista = []
        
        for row in self.board_state2["board"]:
            lista +=[[piece for piece in row]]
        return lista
    
    def lista_figurica1(self):
        ploca = self.board_state1["board"]
        lista = []
        for i in range(12):
            for j in range(12):
                if ploca[i][j]!=None:
                    ploca[i][j]["y"] = i
                    ploca[i][j]["x"] = j
                    lista+=[ploca[i][j]]
        return lista
    
    def lista_figurica2(self):
        ploca = self.board_state2["board"]
        lista = []
        for i in range(12):
            for j in range(12):
                if ploca[i][j]!=None:
                    ploca[i][j]["y"] = i
                    ploca[i][j]["x"] = j
                    lista+=[ploca[i][j]]
        return lista
                


# board1 = Board.from_json(r"""
# {"gameState":"{\"boardState1\":{\"board\":[[{\"id\":0,\"oznaka\":\"C\",\"dim\":12,\"black\":false},null,null,null,null,null,null,null,null,null,null,null],[{\"id\":0,\"oznaka\":\"P\",\"black\":false},{\"id\":1,\"oznaka\":\"P\",\"black\":false},{\"id\":2,\"oznaka\":\"P\",\"black\":false},{\"id\":3,\"oznaka\":\"P\",\"black\":false},{\"id\":4,\"oznaka\":\"P\",\"black\":false},{\"id\":5,\"oznaka\":\"P\",\"black\":false},{\"id\":6,\"oznaka\":\"P\",\"black\":false},{\"id\":7,\"oznaka\":\"P\",\"black\":false},{\"id\":8,\"oznaka\":\"P\",\"black\":false},{\"id\":9,\"oznaka\":\"P\",\"black\":false},{\"id\":10,\"oznaka\":\"P\",\"black\":false},{\"id\":11,\"oznaka\":\"P\",\"black\":false}],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[{\"id\":12,\"oznaka\":\"P\",\"black\":true},{\"id\":13,\"oznaka\":\"P\",\"black\":true},{\"id\":14,\"oznaka\":\"P\",\"black\":true},{\"id\":15,\"oznaka\":\"P\",\"black\":true},{\"id\":16,\"oznaka\":\"P\",\"black\":true},{\"id\":17,\"oznaka\":\"P\",\"black\":true},{\"id\":18,\"oznaka\":\"P\",\"black\":true},{\"id\":19,\"oznaka\":\"P\",\"black\":true},{\"id\":20,\"oznaka\":\"P\",\"black\":true},{\"id\":21,\"oznaka\":\"P\",\"black\":true},{\"id\":22,\"oznaka\":\"P\",\"black\":true},{\"id\":23,\"oznaka\":\"P\",\"black\":true}],[null,{\"id\":1,\"oznaka\":\"K\",\"black\":true},null,null,null,null,null,null,null,null,null,null]],\"whitePiecesPlacement\":[{\"id\":0,\"oznaka\":\"K\",\"black\":false},null,{\"id\":0,\"oznaka\":\"D\",\"black\":false},{\"id\":0,\"oznaka\":\"J\",\"dim\":12,\"black\":false},{\"id\":0,\"oznaka\":\"N\",\"black\":false},{\"id\":1,\"oznaka\":\"N\",\"black\":false},{\"id\":0,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":0,\"oznaka\":\"T\",\"black\":false},{\"id\":1,\"oznaka\":\"T\",\"black\":false},{\"id\":1,\"oznaka\":\"D\",\"black\":false},{\"id\":1,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":0,\"oznaka\":\"S\",\"black\":false},null,null,null,null,null,null,null,null,null,null,null,null],\"whitePijanPlacement\":[],\"blackPiecesPlacement\":[null,{\"id\":1,\"oznaka\":\"C\",\"dim\":12,\"black\":true},{\"id\":2,\"oznaka\":\"D\",\"black\":true},{\"id\":1,\"oznaka\":\"J\",\"dim\":12,\"black\":true},{\"id\":2,\"oznaka\":\"N\",\"black\":true},{\"id\":3,\"oznaka\":\"N\",\"black\":true},{\"id\":2,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":2,\"oznaka\":\"T\",\"black\":true},{\"id\":3,\"oznaka\":\"T\",\"black\":true},{\"id\":3,\"oznaka\":\"D\",\"black\":true},{\"id\":3,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":1,\"oznaka\":\"S\",\"black\":true},null,null,null,null,null,null,null,null,null,null,null,null],\"blackPijanPlacement\":[],\"whiteMoves\":true,\"phase\":1,\"cnt\":2,\"dim\":12},\"boardState2\":{\"board\":[[null,null,null,{\"id\":4,\"oznaka\":\"N\",\"black\":false},null,null,null,null,null,null,null,null],[{\"id\":24,\"oznaka\":\"P\",\"black\":false},{\"id\":25,\"oznaka\":\"P\",\"black\":false},{\"id\":26,\"oznaka\":\"P\",\"black\":false},{\"id\":27,\"oznaka\":\"P\",\"black\":false},{\"id\":28,\"oznaka\":\"P\",\"black\":false},{\"id\":29,\"oznaka\":\"P\",\"black\":false},{\"id\":30,\"oznaka\":\"P\",\"black\":false},{\"id\":31,\"oznaka\":\"P\",\"black\":false},{\"id\":32,\"oznaka\":\"P\",\"black\":false},{\"id\":33,\"oznaka\":\"P\",\"black\":false},{\"id\":34,\"oznaka\":\"P\",\"black\":false},{\"id\":35,\"oznaka\":\"P\",\"black\":false}],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[{\"id\":36,\"oznaka\":\"P\",\"black\":true},{\"id\":37,\"oznaka\":\"P\",\"black\":true},{\"id\":38,\"oznaka\":\"P\",\"black\":true},{\"id\":39,\"oznaka\":\"P\",\"black\":true},{\"id\":40,\"oznaka\":\"P\",\"black\":true},{\"id\":41,\"oznaka\":\"P\",\"black\":true},{\"id\":42,\"oznaka\":\"P\",\"black\":true},{\"id\":43,\"oznaka\":\"P\",\"black\":true},{\"id\":44,\"oznaka\":\"P\",\"black\":true},{\"id\":45,\"oznaka\":\"P\",\"black\":true},{\"id\":46,\"oznaka\":\"P\",\"black\":true},{\"id\":47,\"oznaka\":\"P\",\"black\":true}],[null,null,null,{\"id\":3,\"oznaka\":\"S\",\"black\":true},null,null,null,null,null,null,null,null]],\"whitePiecesPlacement\":[{\"id\":2,\"oznaka\":\"K\",\"black\":false},{\"id\":2,\"oznaka\":\"C\",\"dim\":12,\"black\":false},{\"id\":4,\"oznaka\":\"D\",\"black\":false},{\"id\":2,\"oznaka\":\"J\",\"dim\":12,\"black\":false},null,{\"id\":5,\"oznaka\":\"N\",\"black\":false},{\"id\":4,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":4,\"oznaka\":\"T\",\"black\":false},{\"id\":5,\"oznaka\":\"T\",\"black\":false},{\"id\":5,\"oznaka\":\"D\",\"black\":false},{\"id\":5,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":2,\"oznaka\":\"S\",\"black\":false},null,null,null,null,null,null,null,null,null,null,null,null],\"whitePijanPlacement\":[],\"blackPiecesPlacement\":[{\"id\":3,\"oznaka\":\"K\",\"black\":true},{\"id\":3,\"oznaka\":\"C\",\"dim\":12,\"black\":true},{\"id\":6,\"oznaka\":\"D\",\"black\":true},{\"id\":3,\"oznaka\":\"J\",\"dim\":12,\"black\":true},{\"id\":6,\"oznaka\":\"N\",\"black\":true},{\"id\":7,\"oznaka\":\"N\",\"black\":true},{\"id\":6,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":6,\"oznaka\":\"T\",\"black\":true},{\"id\":7,\"oznaka\":\"T\",\"black\":true},{\"id\":7,\"oznaka\":\"D\",\"black\":true},{\"id\":7,\"oznaka\":\"L\",\"dim\":12,\"black\":true},null,null,null,null,null,null,null,null,null,null,null,null,null],\"blackPijanPlacement\":[],\"whiteMoves\":true,\"phase\":1,\"cnt\":2,\"dim\":12},\"status\":\"Draw\",\"illegalMoveCounter\":0}"}
# """)
# board1.print_board()
# board1 = Board.from_json(r"""
# {"gameState":"{\"boardState1\":{\"board\":[[null,{\"id\":0,\"oznaka\":\"N\",\"black\":false},null,null,null,null,null,null,null,null,null,null],[{\"id\":0,\"oznaka\":\"P\",\"black\":false},{\"id\":1,\"oznaka\":\"P\",\"black\":false},{\"id\":2,\"oznaka\":\"P\",\"black\":false},{\"id\":3,\"oznaka\":\"P\",\"black\":false},{\"id\":4,\"oznaka\":\"P\",\"black\":false},{\"id\":5,\"oznaka\":\"P\",\"black\":false},{\"id\":6,\"oznaka\":\"P\",\"black\":false},{\"id\":7,\"oznaka\":\"P\",\"black\":false},{\"id\":8,\"oznaka\":\"P\",\"black\":false},{\"id\":9,\"oznaka\":\"P\",\"black\":false},{\"id\":10,\"oznaka\":\"P\",\"black\":false},{\"id\":11,\"oznaka\":\"P\",\"black\":false}],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[{\"id\":12,\"oznaka\":\"P\",\"black\":true},{\"id\":13,\"oznaka\":\"P\",\"black\":true},{\"id\":14,\"oznaka\":\"P\",\"black\":true},{\"id\":15,\"oznaka\":\"P\",\"black\":true},{\"id\":16,\"oznaka\":\"P\",\"black\":true},{\"id\":17,\"oznaka\":\"P\",\"black\":true},{\"id\":18,\"oznaka\":\"P\",\"black\":true},{\"id\":19,\"oznaka\":\"P\",\"black\":true},{\"id\":20,\"oznaka\":\"P\",\"black\":true},{\"id\":21,\"oznaka\":\"P\",\"black\":true},{\"id\":22,\"oznaka\":\"P\",\"black\":true},{\"id\":23,\"oznaka\":\"P\",\"black\":true}],[null,null,null,null,null,null,null,null,null,null,null,null]],\"whitePiecesPlacement\":[{\"id\":0,\"oznaka\":\"K\",\"black\":false},{\"id\":0,\"oznaka\":\"C\",\"dim\":12,\"black\":false},{\"id\":0,\"oznaka\":\"D\",\"black\":false},{\"id\":0,\"oznaka\":\"J\",\"dim\":12,\"black\":false},null,{\"id\":1,\"oznaka\":\"N\",\"black\":false},{\"id\":0,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":0,\"oznaka\":\"T\",\"black\":false},{\"id\":1,\"oznaka\":\"T\",\"black\":false},{\"id\":1,\"oznaka\":\"D\",\"black\":false},{\"id\":1,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":0,\"oznaka\":\"S\",\"black\":false},null,null,null,null,null,null,null,null,null,null,null,null],\"whitePijanPlacement\":[],\"blackPiecesPlacement\":[{\"id\":1,\"oznaka\":\"K\",\"black\":true},{\"id\":1,\"oznaka\":\"C\",\"dim\":12,\"black\":true},{\"id\":2,\"oznaka\":\"D\",\"black\":true},{\"id\":1,\"oznaka\":\"J\",\"dim\":12,\"black\":true},{\"id\":2,\"oznaka\":\"N\",\"black\":true},{\"id\":3,\"oznaka\":\"N\",\"black\":true},{\"id\":2,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":2,\"oznaka\":\"T\",\"black\":true},{\"id\":3,\"oznaka\":\"T\",\"black\":true},{\"id\":3,\"oznaka\":\"D\",\"black\":true},{\"id\":3,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":1,\"oznaka\":\"S\",\"black\":true},null,null,null,null,null,null,null,null,null,null,null,null],\"blackPijanPlacement\":[],\"whiteMoves\":false,\"phase\":1,\"cnt\":1,\"dim\":12},\"boardState2\":{\"board\":[[{\"id\":2,\"oznaka\":\"K\",\"black\":false},null,null,null,null,null,null,null,null,null,null,null],[{\"id\":24,\"oznaka\":\"P\",\"black\":false},{\"id\":25,\"oznaka\":\"P\",\"black\":false},{\"id\":26,\"oznaka\":\"P\",\"black\":false},{\"id\":27,\"oznaka\":\"P\",\"black\":false},{\"id\":28,\"oznaka\":\"P\",\"black\":false},{\"id\":29,\"oznaka\":\"P\",\"black\":false},{\"id\":30,\"oznaka\":\"P\",\"black\":false},{\"id\":31,\"oznaka\":\"P\",\"black\":false},{\"id\":32,\"oznaka\":\"P\",\"black\":false},{\"id\":33,\"oznaka\":\"P\",\"black\":false},{\"id\":34,\"oznaka\":\"P\",\"black\":false},{\"id\":35,\"oznaka\":\"P\",\"black\":false}],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null,null,null,null],[{\"id\":36,\"oznaka\":\"P\",\"black\":true},{\"id\":37,\"oznaka\":\"P\",\"black\":true},{\"id\":38,\"oznaka\":\"P\",\"black\":true},{\"id\":39,\"oznaka\":\"P\",\"black\":true},{\"id\":40,\"oznaka\":\"P\",\"black\":true},{\"id\":41,\"oznaka\":\"P\",\"black\":true},{\"id\":42,\"oznaka\":\"P\",\"black\":true},{\"id\":43,\"oznaka\":\"P\",\"black\":true},{\"id\":44,\"oznaka\":\"P\",\"black\":true},{\"id\":45,\"oznaka\":\"P\",\"black\":true},{\"id\":46,\"oznaka\":\"P\",\"black\":true},{\"id\":47,\"oznaka\":\"P\",\"black\":true}],[null,null,null,null,null,null,null,null,null,null,null,null]],\"whitePiecesPlacement\":[null,{\"id\":2,\"oznaka\":\"C\",\"dim\":12,\"black\":false},{\"id\":4,\"oznaka\":\"D\",\"black\":false},{\"id\":2,\"oznaka\":\"J\",\"dim\":12,\"black\":false},{\"id\":4,\"oznaka\":\"N\",\"black\":false},{\"id\":5,\"oznaka\":\"N\",\"black\":false},{\"id\":4,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":4,\"oznaka\":\"T\",\"black\":false},{\"id\":5,\"oznaka\":\"T\",\"black\":false},{\"id\":5,\"oznaka\":\"D\",\"black\":false},{\"id\":5,\"oznaka\":\"L\",\"dim\":12,\"black\":false},{\"id\":2,\"oznaka\":\"S\",\"black\":false},null,null,null,null,null,null,null,null,null,null,null,null],\"whitePijanPlacement\":[],\"blackPiecesPlacement\":[{\"id\":3,\"oznaka\":\"K\",\"black\":true},{\"id\":3,\"oznaka\":\"C\",\"dim\":12,\"black\":true},{\"id\":6,\"oznaka\":\"D\",\"black\":true},{\"id\":3,\"oznaka\":\"J\",\"dim\":12,\"black\":true},{\"id\":6,\"oznaka\":\"N\",\"black\":true},{\"id\":7,\"oznaka\":\"N\",\"black\":true},{\"id\":6,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":6,\"oznaka\":\"T\",\"black\":true},{\"id\":7,\"oznaka\":\"T\",\"black\":true},{\"id\":7,\"oznaka\":\"D\",\"black\":true},{\"id\":7,\"oznaka\":\"L\",\"dim\":12,\"black\":true},{\"id\":3,\"oznaka\":\"S\",\"black\":true},null,null,null,null,null,null,null,null,null,null,null,null],\"blackPijanPlacement\":[],\"whiteMoves\":false,\"phase\":1,\"cnt\":1,\"dim\":12},\"status\":\"Draw\",\"illegalMoveCounter\":0}"}


# """)
# board1.print_board()
# #print(board1.whiteMoves1)

#print(board1.lista_figurica2())
#board1.print_board()
#list1 = board1.get_board1()
#print(list1)
#piece1 = Piece.from_dict(list1[0][1])
#print(piece1.isblack)
#print(piece1.type)
#print(piece1.id)
#print(board1.whiteMoves1)

