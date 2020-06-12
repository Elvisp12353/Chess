import pieces,board

black_pieces = pieces.generate_pieces("black")
black_pieces = pieces.generate_pieces("white")
board = board.generate_board() 

def show_board(board):
        """This function show the board in a organized way"""
        for line in board:
            print(line)

def put_in_start_position(pieces,color,board):
   
   if color=="black":
    board.obj[0] = pieces[0]
    board.obj[1] = pieces[1]
   else:
    board.obj[7] = pieces[0]
    board.obj[6] = pieces[1]
   return board.show_board(board.obj)

def change_to_icon(board):
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


put_in_start_position(black_pieces,"black",board)
put_in_start_position(black_pieces,"white",board)

print(show_board(change_to_icon(board.obj)))

