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
    def __init__(self,icon,color):
        self.icon = icon
        self.color = color
    
class king(piece):
    def __init__(self,color):        
        self.color = color
        if(self.color =="white"):
            self.icon = "♔"
        else:
            self.icon = "♚"
    
    def move(self):
        pass

class queen(piece):
    def __init__(self,color):
        self.color = color
        if(self.color =="white"):
            self.icon = "♕"
        else:
            self.icon = "♛"        
    
    def move(self):
        pass

class rook(piece):
    def __init__(self,color):        
        self.color = color

        if(self.color =="white"):
            self.icon = "♖"
        else:
            self.icon = "♜"

    def move(self):
        pass



class bishops(piece):
    def __init__(self,color):        
        self.color = color
        if(self.color =="white"):
            self.icon = "♗"
        else:
            self.icon = "♝"
    def move(self):
        pass



class knights(piece):
    def __init__(self,color):          
        self.color = color
        if(self.color =="white"):
            self.icon = "♘"
        else:
            self.icon = "♞"
    def move(self):
        pass

class pawn(piece):
    def __init__(self,color):       
        self.color = color
        if(self.color =="white"):
            self.icon = "♙"
        else:
            self.icon = "♟"
    def move(self):
        pass


numbre1 = queen("white")
print(numbre1.icon)