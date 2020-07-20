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

#prepare the  board
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
        
        move = player.player1.turn(board)
        while move == False:
            move = player.player1.turn(board)
        print(show_board(change_to_icon(board.obj)))
        turn = "player2"
    else:
        move = player.player2.turn(board)
        while move == False:
            move = player.player2.turn(board)
        print(show_board(change_to_icon(board.obj)))
        turn = "player1"
    

