
class Piece:
    def __init__(self,color):
        self.color = color
        
    def set_moves(self, pos , board):
        pass
         
    def getMoves(self , position , board):
        #logic for moves
        
        return []
      
      
#creating a Pawn pievc extending the abstract class 

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        
    

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        
    

      

 
    
if  __name__== "__main__":
    
    piece = Piece()
    
    