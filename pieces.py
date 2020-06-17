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
import board
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
    
    def __init__(self,color,x,y,icon,name,moves):
        self.icon = icon
        self.color = color
        self.name = name
        self.x = x
        self.y =y
        self.moves = moves

        if self.color == "white":
            self.icon = white_pieces[self.name]
        else:
            self.icon = black_pieces[self.name]
    def eat(self):
        pass
    def move(self,entry_board,new_X,new_Y):
        if type(entry_board[new_X][new_Y]) == str:
            old_x = self.x
            old_y = self.y
            entry_board[self.x][self.y] = board.replace_spaces(old_x,old_y)
            self.x = new_X
            self.Y = new_Y
            self.moves +=1
            entry_board.moves+=1
            entry_board[new_X][new_Y] = self
            return board
        else:
            if entry_board[new_X][new_Y].color != self.color:
                self.eat()
            else:
                return "This movement can't be done"   
            
class King(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="king",moves=0):   
        Piece.__init__(self,color,x,y,icon,name,moves)        
     
class Queen(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="queen",moves=0):   
        Piece.__init__(self,color,x,y,icon,name,moves)
          
class Rook(Piece):
     def __init__(self,color,x=0,y=0,icon="",name="rook",moves=0):   
        Piece.__init__(self,color,x,y,icon,name,moves)
    
class Bishops(Piece):
     def __init__(self,color,x=0,y=0,icon="",name="bishop",moves=0):   
        Piece.__init__(self,color,x,y,icon,name,moves)

class Knights(Piece):
     def __init__(self,color,x=0,y=0,icon="",name="knight",moves=0):   
        Piece.__init__(self,color,x,y,icon,name,moves)

class Pawn(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="pawn",moves=0):   
        Piece.__init__(self,color,x,y,icon,name,moves=0)

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

  
 