import pieces,board,player

black_pieces = pieces.generate_pieces("black")
white_pieces = pieces.generate_pieces("white")
board = board.generate_board() 

def show_board(board):
        """This function show the board in a organized way"""
        for line in board:
            print(line)
        return " "
     
def add_position_to_the_pieces(pieces,color):
    """This function adds the initial position where the pieces are going to be """
    if color == "black":
        row_1 = 0
        row_2 = 1
    else:
        row_1 = 7
        row_2 = 6
    for row in pieces:
        y =0
        for  piece in row:
            if pieces.index(row) == 0:
                piece.x = row_1
            else:
                piece.x = row_2
            piece.y = y
            y+=1

def put_in_start_position(pieces,color,board):
    
   """Put the pieces into the board based on their respective positions"""
   
   if color=="black":    
    board.obj[0] = pieces[0]
    board.obj[1] = pieces[1]
   else:
    board.obj[7] = pieces[0]
    board.obj[6] = pieces[1]
   return board.show_board(board.obj)

def change_to_icon(board):
    """This function shows the icons instead of the objets name so the player can understand better the game"""
    changed_board = []
    new_line = []
    for line in board:
        for square in line:
            if type(square) != str:
                new_line.append(square.icon)
                if len(new_line) == 8:
                    changed_board.append(new_line)
                    new_line = []
            else:
                new_line.append(square)
                if len(new_line) == 8:
                    changed_board.append(new_line)
                    new_line = []

    return changed_board

def get_avaible_pieces(board):
    black_pieces =[]
    white_pieces =[]
    for line in board:
        for square in line:            
            if type(square) != str:
                if square.color == "black":
                    black_pieces.append(square)
                else:
                    white_pieces.append(square)
    return black_pieces,white_pieces

def get_king_position(color,board):
    for line in board:
        for square in line:
            if type(square) != str:
                if square.name == "king" and square.color == color:
                    return square

def get_king_avaible_positions(king):
    positions =[]    
    for x in range(-1,2):        
        for y in range(-1,2):
            if [king.x+x,king.y+y] != [king.x,king.y] and king.x+x <8 and king.x+x >-1 and king.y+y <8 and king.y+y >-1 :
                if pieces.validate_movement(king,king.x+x,king.y+y,board.obj) == True:
                    positions.append([king.x+x,king.y+y])
    return positions        

def can_king_move(king,board):
    avaible_pieces = get_avaible_pieces(board.obj)
    if king.color == "black":
        enemy_pieces = avaible_pieces[1]
    else:
        enemy_pieces = avaible_pieces[0]

    positions = get_king_avaible_positions(king)
    for position in positions:
        for piece in enemy_pieces:
            if pieces.validate_movement(piece,position[0],position[1],board.obj) == True and pieces.find_obstacle(piece,position[0],position[1],board.obj) == True:
                positions.remove(position)
    if len(positions) >0:
        return positions
    else:
        return False                

def king_check(color):
    avaible_pieces = get_avaible_pieces(board.obj)
    if color == "black":
        king_color = "white"
        enemy_pieces = avaible_pieces[1]
        allies = avaible_pieces[0]
    else:
        king_color = "black"
        enemy_pieces = avaible_pieces[0]
        allies = avaible_pieces[1]
        
    king = get_king_position(king_color,board.obj)
    
    for piece in enemy_pieces:
        if pieces.validate_movement(piece,king.x,king.y,board.obj) == True and pieces.find_obstacle(piece,king.x,king.y,board.obj) == True:
            board.obj[king.x][king.y].safe = False
            king_is_checkmate = king_checkmate(king,enemy_pieces,allies)
            if  king_is_checkmate == True:
                print(turn," king is checkmate game ended")
                exit()
            else:
                return king_is_checkmate

        else:
            board.obj[king.x][king.y].safe = True
            return True

def king_checkmate(king,enemies,allies):
    dangerous_pieces = []
    movements = []
    for piece in enemies:
        if pieces.validate_movement(piece,king.x,king.y,board.obj) == True and pieces.find_obstacle(piece,king.x,king.y,board.obj) == True:
            dangerous_pieces.append([piece,pieces.make_a_path(piece,king.x,king.y,board.obj)])
        
    if can_king_move != False:
        movements.append([king.x,king.y])

    for piece in dangerous_pieces:
        for allie in allies:
            if pieces.validate_movement(allie,piece.x,piece.y,board.obj) == True and pieces.find_obstacle(allie,piece.x,piece.y,board.obj) == True:
                movements.append([allie.x,allie.y])

        for space in pieces.make_a_path(piece,king.x,king.y,board.obj):
            for allie in allies:
                if pieces.validate_movement(allie,space[0],space[1],board.obj) == True and pieces.find_obstacle(allie,space[0],space[1],board.obj) == True:
                    movements.append([allie.x,allie.y])
    if len(movements) == 0:
        return True
    else:
        return movements
#prepare the board
def start_game():
    """This function calls all the functions needed to start a new game"""
    add_position_to_the_pieces(black_pieces,"black")
    add_position_to_the_pieces(white_pieces,"white")
    put_in_start_position(black_pieces,"black",board)
    put_in_start_position(white_pieces,"white",board)  
    print(show_board(change_to_icon(board.obj)))

# here starts the game loop

answer  = input("Welcome to chess \nselect 1 to start a game \nselect 2 to read the rules\n")
if answer == "1":
    start_game()
elif answer == "2":
    print("""Here i'll explain how to use this program if you need any information about how to play chess go to:\nhttps://www.chess.com/learn-how-to-play-chess\nFor playing this game you need  to first select the action you want to do (1 for moving and 3 for surrender)\nif you want to move a piece first you need to put where it is in with a position based on x and y\n(by example 00 without spaces) and then the position where you want to move it (40 by example).""")
    exit()
else:
    print("invalid input")

turn = "player1"

while True:
    
    if turn == "player1":
        king_is_check = king_check("white")
        while  king_is_check != True:
            print("Your King is on check protect it \n these are your avaible pieces to move:\n", king_is_check ,"\n select the one you're going to move")
            piece = input()
            while piece not in king_is_check:
                print("Your king is in danger move another piece")
            print("where do you want to move it")
            new = input()
            board.obj[int(piece[0])][int(piece[1])].move(board,int(new[0]),int(new[1]),turn)
            

        move = player.player1.turn(board)
        while move == False:
            move = player.player1.turn(board)
        print(show_board(change_to_icon(board.obj)))
        turn = "player2"

    else:
        king_is_check = king_check("black")
        while  king_is_check != True:
            print("Your King is on check protect it \n these are your avaible pieces to move:\n", king_is_check ,"\n select the one you're going to move")
            piece = input()
            while piece not in king_is_check:
                print("Your king is in danger move another piece")
            print("where do you want to move it")
            new = input()
            board.obj[int(piece[0])][int(piece[1])].move(board,int(new[0]),int(new[1]),turn)
            
        move = player.player2.turn(board)
        while move == False:
            move = player.player2.turn(board)
        print(show_board(change_to_icon(board.obj)))
        turn = "player1"