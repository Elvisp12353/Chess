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
This module make the board
"""

class Board(object):
    """This is the board object"""
    def __init__(self,moves=0):
        self.obj = self.make_board()
    
    def make_board(self):
        """This function make the board"""
        matrix =[]  #This is the matrix that'll contain the board    
        line =[]    #This contain the lines 
            
        for  i in range(4):     
            i = i
            line.append("⬜")
            line.append("⬛")           
                
        for block_number in range(8):            
            if block_number %2 == 0:     
                matrix.append(line)                
            else:
                matrix.append(line[::-1])
        return matrix 

    def show_board(self,board):
        """This function show the board in a organized way"""
        for line in range(8):
            for element in range(8):
                if type(board[line][element]) == object:
                    board[line][element] = element.icon

        return board


        
    
def generate_board():
    New_board = Board()
    New_board.make_board()
    return New_board

def replace_spaces(x,y):
    if x %2 ==0 and y %2 !=0:
        return "⬜"
    elif x %2 !=0 and y %2 ==0:
        return "⬜"
    else:
        return "⬛"