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
        """This function determinates if the movement that the player is trying to do is valid 
        if its not valid the function returns false and the player have to choose another movement"""
        board_list = entry_board.obj 
        def change_position():
            board_list[self.x][self.y] = board.replace_spaces(self.x,self.y)     
            self.x = new_X
            self.Y = new_Y
            self.moves +=1
            entry_board.moves+=1
            board_list[new_X][new_Y] = self
            return board

        if validate_movement(self,new_X,new_Y,type(board_list[new_X][new_Y])) == False:
            print("Invalid movement")
            return False
        if self.name != "knight":  
            if find_obstacle(self,new_X,new_Y,entry_board.obj) == False:
                print("There's a piece in the way")
                return False
        
        if type(board_list[new_X][new_Y]) == str:#here i check if the space is empty
            change_position()     

        else:#if is not empty compare the color of the pieces
            if board_list[new_X][new_Y].color != self.color:# if the colors of the pieces is diferent move the pieces
                change_position()
            
            else:
                print("You can't eat your own pieces") 
                return False
        
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

def find_obstacle(piece_to_move,new_x,new_y,board):
    
    spaces =[]
    diagonal_position =[]
    move_distance_x = new_x - piece_to_move.x
    move_distance_y = new_y - piece_to_move.y
    diagonal_position.append(move_distance_x)
    diagonal_position.append(-(new_x - piece_to_move.x) )

    def compare_diagonal():
        if new_x < piece_to_move.x:
            if new_y < piece_to_move.y:
                for distance in range(abs(move_distance_x)):
                    spaces.append([piece_to_move.x-1,piece_to_move.y-1])
            else:
                for distance in range(move_distance_y):
                    spaces.append([piece_to_move.x-1,piece_to_move.y+1])
        else:
            if new_y > piece_to_move.y:
                for distance in range(move_distance_x):
                    spaces.append([piece_to_move.x+1,piece_to_move.y+1])
            else:
                for distance in range(move_distance_x):
                    spaces.append([piece_to_move.x+1,piece_to_move.y-1])

    if move_distance_x in[1,-1] and move_distance_y in[1,-1]:
        return True
    
    elif new_x != piece_to_move.x and new_y == piece_to_move.y:             
        for x in range(piece_to_move.x,new_x):
            if [x,piece_to_move.y] != [piece_to_move.x,piece_to_move.y]:
                spaces.append([x,piece_to_move.y])
    
    elif piece_to_move.y != new_y and piece_to_move.x == new_x:
        for y in range(piece_to_move.y ,new_y):
            if [piece_to_move.x,y] == [piece_to_move.x,piece_to_move.y]:
                spaces.append([piece_to_move.x,y])
    
    if new_y - piece_to_move.y in diagonal_position:
        compare_diagonal()
        
    
    for space in spaces:
        
        if type(board[space[0]][space[1]]) != str:
            return False
    return True

def validate_movement(piece_to_move,new_x,New_y,space_type):
    diagonal_position =[]
    move_distance_x = new_x - piece_to_move.x
    move_distance_y = New_y - piece_to_move.y
    diagonal_position.append(move_distance_x)
    diagonal_position.append(-(new_x - piece_to_move.x)) 
    
    if  new_x > 7 or New_y >7:
        return False 
    elif piece_to_move.name == "king":
        if move_distance_x in [0,1,-1] and move_distance_y in [0,1,-1]:
            return True
        else:
            return False                 
    elif piece_to_move.name == "queen":
        if new_x != piece_to_move.x and New_y == piece_to_move.y or piece_to_move.y != New_y and piece_to_move.x == new_x:            
            return True
        if New_y - piece_to_move.y in diagonal_position:
            return True
        else:
            return False            
    elif piece_to_move.name == "rook":
    
        if new_x != piece_to_move.x and New_y == piece_to_move.y or piece_to_move.y != New_y and piece_to_move.x == new_x:            
            return True 
        else:
            return False
    elif piece_to_move.name =="bishop":
        
        if New_y - piece_to_move.y in diagonal_position:
            return True
        else:
            return False
        return False
    elif piece_to_move.name == "knight":
        if move_distance_x in [2,-2] and move_distance_y - New_y in [1,-1]:
            return True 
        elif move_distance_y in [2,-2] and move_distance_x in [1,-1]:
            return True
        else:
            return False
    elif piece_to_move.name == "pawn":

        if piece_to_move.color == "black":
            if piece_to_move.x > new_x:
                return False
        else:
            if piece_to_move.x < new_x:
                return False

        if piece_to_move.moves <1:
            
            if space_type == str:
                
                if move_distance_x in [1,-1,2,-2] and piece_to_move.y == New_y:
                    return True
                return False
        else:
            if space_type == str:
                if move_distance_x in [1,-1] and piece_to_move.y == New_y:
                    return True
            
            elif  move_distance_x in [1,-1] and move_distance_y in [1,-1]:
                if space_type != str:
                    return True
            return False
    else:
        print("Error")
     