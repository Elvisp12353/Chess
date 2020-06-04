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
    def __init__(self):
        self.obj = self.make_board()
    
    def make_board(self):
        matriz =[]      
        line =[]
        
        for  i in range(4):     
            line.append("⬜")
            line.append("⬛")
        
        
        for i in range(8):            
            if i %2 == 0:     
                matriz.append(line)                
            else:
                matriz.append(line[::-1])
        return matriz 

    def show_board(self):
        for element in range(8):
            print(self.obj[element])
        
    
n = board()
n.show_board()