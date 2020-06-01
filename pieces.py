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
class piece(object):
    def __init__(self,icon):
        self.icon = icon
        

class king(piece):
    def __init__(self):
        self.icon = "♚"

    
class queen(piece):
    def __init__(self):
        self.icon = "♛"
  

class rook(piece):
    def __init__(self):
        self.icon = "♜"
        

class bishops(piece):
    def __init__(self):
        self.icon = "♝"

class knights(piece):
    def __init__(self):
        self.icon = "♞"

class pawn(piece):
    def __init__(self):
        self.icon = "♟"


numbre1 = pawn()
print(numbre1.icon)