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
    
    def __init__(self,color,icon,name):
        self.icon = icon
        self.color = color
        self.name = name
        if self.color == "white":
            self.icon = white_pieces[self.name]
        else:
            self.icon = black_pieces[self.name]

    def move(self):
        pass
    
class King(Piece):
    def __init__(self,color,icon="",name="king"):   
        Piece.__init__(self,color,icon,name)        
     

class Queen(Piece):
    def __init__(self,color,icon="",name="queen"):   
        Piece.__init__(self,color,icon,name)
    
        

class Rook(Piece):
     def __init__(self,color,icon="",name="rook"):   
        Piece.__init__(self,color,icon,name)
  
   

class Bishops(Piece):
     def __init__(self,color,icon="",name="bishop"):   
        Piece.__init__(self,color,icon,name)

class Knights(Piece):
     def __init__(self,color,icon="",name="knight"):   
        Piece.__init__(self,color,icon,name)


class Pawn(Piece):
    def __init__(self,color,icon="",name="pawn"):   
        Piece.__init__(self,color,icon,name)

  
 