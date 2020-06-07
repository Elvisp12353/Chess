import pieces,board
def generate_pieces(color="black"):
    
    pawns =[]
    line = []
    for each in range(8):
        pawns.append(pieces.pawn(color).icon)
        if each < 2: 
            if each == 1:
                line.append(pieces.queen(color).icon)
                line.append(pieces.king(color).icon)           
            line.append(pieces.rook(color).icon)
            line.append(pieces.bishops(color).icon)
            line.append(pieces.knights(color).icon)
    

    return line,pawns



def generate_board():
    New_board = board.board()
    New_board.make_board()
    return New_board

def order_board(board):
    for element in board:
        print(element)

def replace_pieces():
   board = generate_board()  

   black_pieces = generate_pieces("black")
   white_pieces = generate_pieces("white")
   
   board.obj[0] = black_pieces[0]
   board.obj[1] = black_pieces[1]

   board.obj[7] = white_pieces[0]
   board.obj[6] = white_pieces[1]
   
   return order_board(board.obj)
    
   
   



replace_pieces()