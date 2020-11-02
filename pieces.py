#!/ust/bin/python3
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
    """
    This is the main class for all the pieces it have the properties:
    
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
        self.icon = white_pieces[self.name] if self.color == "white" else black_pieces[self.name]
    
    def to_crown(self,entry_board):
            """
            This function exchange the pawn for another piece 
            when it reach the other side of the board
            """
            exchangable_pieces ={
            1: Queen(self.color,self.x,self.y),
            2: Rook(self.color,self.x,self.y),
            3: Bishops(self.color,self.x,self.y),
            4: Knights(self.color,self.x,self.y)
            }
            selection = int(input("Select for which piece you want to exchange your pawn:\nselect 1 for Queen\nselect 2 for Rook\nselect 3 for Bishop\nselect 4 for Knigth"))
            
            entry_board.obj[self.x][self.y] = exchangable_pieces[selection]
            return entry_board

    def move(self,entry_board,new_X,new_Y,player,move_type="default"):
        """This function determinates if the movement that the player is trying to do is valid 
        if its not valid the function returns false and the player have to choose another movement"""
        
        board_matrix = entry_board.obj 
        if player.color != self.color:
            print(player.color)
            print("You can't move the other player's pieces")
            return False
        
        if validate_movement(self,new_X,new_Y,board_matrix) == False and move_type == "default":
            print("Invalid movement")
            return False

        if self.name != "knight" and move_type == "default":  
            if find_obstacle(self,new_X,new_Y,entry_board.obj) == False:
                print("There's a piece in the way")
                return False
        
        board_matrix[self.x][self.y] = board.replace_spaces(self.x,self.y)   
        self.x = new_X
        self.y = new_Y
        self.moves +=1
        entry_board.moves+=1
        board_matrix[new_X][new_Y] = self
        
        if self.name == "pawn":
            if self.color == "black" and self.x ==7 or self.color == "white" and self.x ==0:
                self.to_crown(entry_board)
         
        return board
        
        
class King(Piece):
    def __init__(self,color,x=0,y=0,icon="",name="king",moves=0,safe=True):   
        Piece.__init__(self,color,x,y,icon,name,moves)
        self.safe = safe  
    
    def castling(self,rook,entry_board,player):       
        if find_obstacle(self,rook.x,rook.y,entry_board.obj) == False:            
            return False

        if rook.y < self.y:
            self.move(entry_board,self.x,self.y-2,player,"castling")
            rook.move(entry_board,self.x,self.y+1,player,"castling")            
        else:
            self.move(entry_board,self.x,self.y+2,player,"castling")
            rook.move(entry_board,self.x,self.y-1,player,"castling")      
     
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
    """This function make all the piece objets that the game is gonna use""" 
    pawns =[]
    line = []

    for each in range(8):       
        pawns.append(Pawn(color))
    
    line.append(Queen(color))
    line.append(King(color)) 
    line.append(Bishops(color))  
    line.append(Knights(color))
    line.append(Rook(color))                        
    line.append(Rook(color))
    line.append(Knights(color))
    line.append(Bishops(color))             
    return line,pawns

def make_a_path(piece_to_move,new_x,new_y,entry_board):
    """
    this function creates a list with all the spaces that a piece cross to reach certain position
    """
    spaces =[]
    move_distance_x = new_x - piece_to_move.x
    move_distance_y = new_y - piece_to_move.y
    diagonal_position =[move_distance_x,-(new_x - piece_to_move.x)]
    
    if move_distance_x in[1,-1] and move_distance_y in[1,-1]:# if the piece only move 1 step return true
        return True
    
    #if the piece move add all the positions between the actual position and the new position 
    elif new_x != piece_to_move.x and new_y == piece_to_move.y:# vertical movement
        if piece_to_move.x < new_x:                     
            for x in range(piece_to_move.x,new_x):
                           
                if [x,piece_to_move.y] not in [[piece_to_move.x,piece_to_move.y],[new_x,new_y]]:
                    spaces.append([x,piece_to_move.y])
        else:   
            for x in range(new_x,piece_to_move.x):           
                if [x,piece_to_move.y] not in [[piece_to_move.x,piece_to_move.y],[new_x,new_y]]:
                    spaces.append([x,piece_to_move.y])

    elif piece_to_move.y != new_y and piece_to_move.x == new_x:# horizontal movement
        
        if piece_to_move.y < new_y:
            
            for y in range(piece_to_move.y ,new_y):                             
                if [piece_to_move.x,y] not in [[piece_to_move.x,piece_to_move.y],[new_x,new_y]]:
                    spaces.append([piece_to_move.x,y])
        else:            
            for y in range(new_y,piece_to_move.y):                             
                if [piece_to_move.x,y] not in [[piece_to_move.x,piece_to_move.y],[new_x,new_y]]:
                    spaces.append([piece_to_move.x,y])

    elif new_y - piece_to_move.y in diagonal_position:#Diagonal movement
        x = piece_to_move.x
        y = piece_to_move.y
        if new_x < piece_to_move.x:
            if new_y < y:
                for distance in range(abs(move_distance_x)):
                    distance +=1
                    x = x -1
                    y = y -1
                    if [x,y] != [new_x,new_y]:
                        spaces.append([x,y])
               
            else:
                for distance in range(move_distance_y):
                    x = x -1
                    y = y +1
                    if [x,y] != [new_x,new_y]:
                        spaces.append([x,y])
                
        else:
            if new_y > piece_to_move.y:
                for distance in range(move_distance_x):
                    x = x +1
                    y = y +1
                    if [x,y] != [new_x,new_y]:
                        spaces.append([x,y])
                
            else:
                for distance in range(move_distance_x):
                    x = x +1
                    y = y -1
                    if [x,y] != [new_x,new_y]:
                        spaces.append([x,y])
                   
    return spaces

def find_obstacle(piece_to_move,new_x,new_y,entry_board):
    """
    This function checks if there's a piece between the piece the player wants to move and it's destiny
    """
    spaces = make_a_path(piece_to_move,new_x,new_y,entry_board)
    
    #compare if in the positions between the actual position and the new one there's a piece
    if spaces == True:
        return True 
    
    for space in spaces:        
        if type(entry_board[space[0]][space[1]]) != str:            
            return False
    return True

def validate_movement(piece_to_move,new_x,New_y,board,movement_type="default"):
    """
    This function verifies if the movement that the player is trying to do is legal
    """
    space_type = type(board[new_x][New_y])
    move_distance_x = new_x - piece_to_move.x
    move_distance_y = New_y - piece_to_move.y
    diagonal_position = [move_distance_x,-(new_x - piece_to_move.x)]

    if type(board[new_x][New_y]) != str:#here i check if the space is empty if is not compare the color of the pieces
             if board[new_x][New_y].color == piece_to_move.color:# if the colors of the pieces is diferent move the pieces
                return False    
    
    if piece_to_move.name == "king":
        if move_distance_x in [0,1,-1] and move_distance_y in [0,1,-1]:
            return True
        elif piece_to_move.x == new_x and move_distance_y == 2 and movement_type == "castling":
            return True
                        
    elif piece_to_move.name == "queen":
        if new_x != piece_to_move.x and New_y == piece_to_move.y or piece_to_move.y != New_y and piece_to_move.x == new_x:            
            return True

        if New_y - piece_to_move.y  in diagonal_position:
            return True
                  
    elif piece_to_move.name == "rook":
    
        if new_x != piece_to_move.x and New_y == piece_to_move.y or piece_to_move.y != New_y and piece_to_move.x == new_x:            
            return True 
       
    elif piece_to_move.name =="bishop":
        if New_y - piece_to_move.y in diagonal_position:
            return True
        
    elif piece_to_move.name == "knight":
        
        if move_distance_x in [2,-2] and move_distance_y  in [1,-1]:
            return True 
        elif move_distance_y in [2,-2] and move_distance_x in [1,-1]:
            return True
        
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
        else:
            if space_type == str:
                if move_distance_x in [1,-1] and piece_to_move.y == New_y:
                    return True
                
                elif type(board[new_x-1][New_y]) != str:
                    if board[new_x-1][New_y].moves == 1 and piece_to_move.x == 4:
                        
                        board[new_x-1][New_y] = board.replace_spaces(new_x-1,New_y)
                        return True
                        
            elif  move_distance_x in [1,-1] and move_distance_y in [1,-1]:                
                if space_type != str:
                    return True
    
    return False      