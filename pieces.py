#!/ust/bin/python3
__author__ ="ELvis Genao"
__copyright__ ="Copyright"
__credits__ ="Elvis"
__license__ ="GPl"
__version__ ="1.0.1"
__maintainer__ ="Elvis Genao"
__email__ ="elvisp12353@gmail.com"
__status__ ="Developer"

"""
This module make the pieces That will be used in the game

"""

#Dictionaries that contains the icons of the pieces
white_pieces={
"king":"♔",
"queen":"♕",
"rook":"♖",
"bishop":"♗",
"knight":"♘",
"pawn":"♙"

}
black_pieces={
"king":"♚",
"queen":"♛",
"rook":"♜",
"bishop":"♝",
"knight":"♞",
"pawn":"♟"

}

class Piece(object):
    
    def __init__(self,color,x,y,icon,name):
        self.icon = icon
        self.color = color
        self.name = name
        self.x = x
        self.y =y

        if self.color == "white":
            self.icon = white_pieces[self.name]
        else:
            self.icon = black_pieces[self.name]

    def move(self,board,x,y):
        if type(board[x][y]) != str:
            board.obj[x][y] = self
            return board
    
class King(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="king"):   
        Piece.__init__(self,color,x,y,icon,name)        
     

class Queen(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="queen"):   
        Piece.__init__(self,color,x,y,icon,name)
    
        

class Rook(Piece):
     def __init__(self,color,x=0,y=0,icon="",name="rook"):   
        Piece.__init__(self,color,x,y,icon,name)
  
   

class Bishops(Piece):
     def __init__(self,color,x=0,y=0,icon="",name="bishop"):   
        Piece.__init__(self,color,x,y,icon,name)

class Knights(Piece):
     def __init__(self,color,x=0,y=0,icon="",name="knight"):   
        Piece.__init__(self,color,x,y,icon,name)


class Pawn(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="pawn"):   
        Piece.__init__(self,color,x,y,icon,name)

def generate_pieces(color):
    
    pawns =[]
    line = []
    for each in range(8):
       
        pawns.append(Pawn(color))
        if each < 2: 
            if each == 1:
                line.append(Queen(color))
                line.append(King(color)) 
                line.append(Bishops(color))  
                line.append(Knights(color))
                line.append(Rook(color))                        
            else:
                line.append(Rook(color))
                line.append(Knights(color))
                line.append(Bishops(color))             
    return line,pawns

  
 