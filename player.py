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
    def __init__(self,color,name):
        self.color = color
        self.name  = name
    def turn(self,board):

        print("""
choose 1 to move a piece
choose 2 to make a special move
choose 3 to give up
        """)
        selection = input()
        if selection == "1":
            selected_piece = input("Choose which piece you wanna move")
            pieceX = selected_piece[0] 
            pieceY = selected_piece[1]
            new_position = input("Choose where you wanna move")
            newX = new_position[0]
            newY = new_position[1]
            return board.obj[int(pieceX)][int(pieceY)].move(board,int(newX),int(newY))        
        elif selection == "2":
            pass        
        elif selection == "3":    
            print(self.name ,"have give up")
        else:
            print("Invalid input")



player1 = player("white","player1")
player2 = player("black","player2")