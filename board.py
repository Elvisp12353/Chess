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

class board(object):
    """This is the board object"""
    def __init__(self):
        self.obj = self.make_board()
    
    def make_board(self):
        """This function make the board"""
        matrix =[]  #This is the matrix that'll contain the board    
        line =[]    #This contain the lines 
        
        for  i in range(4):     
            line.append("⬜")
            line.append("⬛")
        
        
        for block_number in range(8):            
            if block_number %2 == 0:     
                matrix.append(line)                
            else:
                matrix.append(line[::-1])
        return matrix 

    def show_board(self):
        """This function show the board in a organized way"""
        for element in range(8):
            print(self.obj[element])
        
    
