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
This module make the player
"""
class player(object):
    def __init__(self,color,name,castling=True):
        self.color = color
        self.name  = name
        self.castling = castling
    def turn(self,board):

        print( """choose 1 to move a piece \nchoose 2 to give up\nchoose 3 to castle""")
        selection = input()
        if selection == "1":
                try:
                    selected_piece = input("Choose which piece you wanna move")
                    pieceX = selected_piece[0] 
                    pieceY = selected_piece[1]
                    new_position = input("Choose where you wanna move")
                    newX = new_position[0]
                    newY = new_position[1]
                    return board.obj[int(pieceX)][int(pieceY)].move(board,int(newX),int(newY),self)  
                except:
                    print("invalid input")
                    return False
        
        elif selection == "2":    
            print(self.name ,"have give up")

        elif selection == "3":
            if self.castling == True:
                king = input("choose the king")
                king = board.obj[int(king[0])][int(king[1])]
                rook = input("choose")
                rook = board.obj[int(rook[0])][int(rook[1])]
                king.castling(rook,board,self)
                self.castling == False
            else:
                print("You can only make a castling one time")
                return False
        else:
            print("Wrong option")
            return False



player1 = player("white","player1")
player2 = player("black","player2")