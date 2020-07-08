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
"king":" ♔",
"queen":" ♕",
"rook":" ♖",
"bishop":" ♗",
"knight":" ♘",
"pawn":" ♙"
}

black_pieces={
"king":" ♚",
"queen":" ♛",
"rook":" ♜",
"bishop":" ♝",
"knight":" ♞",
"pawn":" ♟"
}



  

class Piece(object):
    """
    This is the father class for all the pieces it have the properties:
    
    icon = The character of the piece
    color = color of the piece
    name = name of the piece (rook, bishop)
    x,y = this is for the position of the piece
    moves = here i count the cuantity of movements of the pieces
    """
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

    

    def move(self,entry_board,new_X,new_Y):
        board_list = entry_board.obj
        valid = validate_movement(self.name,self.x,self.y,new_X,new_Y,self.moves)
        if type(board_list[new_X][new_Y]) == str and valid == True:
                        
            board_list[self.x][self.y] = board.replace_spaces(self.x,self.y)
            board_list[new_X][new_Y] = self       
            self.x = new_X
            self.Y = new_Y
            self.moves +=1
            entry_board.moves+=1
           
            return board
        elif valid == False:
            print("Invalid movement")
        else:
            if board_list[new_X][new_Y].color != self.color:
                print("you must eat not move")
            else:
                print("This movement can't be done") 

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

def find_obstacle():
    pass
def validate_movement(name,x,y,new_x,New_y,moves):
    if name == "king":
        pass  
    elif name == "queen":
        return False
    elif name == "rook":
        if new_x != x and New_y == y or y != New_y and x == new_x:            
            return True
        else:
            return False

    elif name =="bishop":
        return False
    elif name == "knight":
        return False
    elif name == "pawn":
        if moves <1:
            if new_x - x == 1 and y == New_y or new_x - x == -1 and y == New_y:
                return True
            elif new_x - x == 2 and y == New_y or new_x - x == -2 and y == New_y:
                return True
            return False
        else:
            if new_x - x == 1 and y == New_y or new_x - x == -1 and y == New_y:
                return True
            return False
    else:
        print("Error")
    