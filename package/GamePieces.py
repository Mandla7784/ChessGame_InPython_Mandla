
class Piece:
    def __init__(self,color , x ,y):
        self.color = color 
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{self.color} {self.__class__.__name__} at ({self.x} , {self.y} )"
    
    
    #check valid move on a piece 
    def is_valid_move(self , new_x , new_y  ,board):
        
        if self.color == "white":
            if new_x == self.x and new_y == self.y+1 and board[new_x][new_y] is None:
                return True
            
    
        if not (0 <= new_x < len(board) and 0 <= new_y < len(board)):
            return False
        return True
    
        
     #setting a new position of a piece on board   
    def set_moves(self, new_x, new_y , board):
        
        if(new_x > 0 and new_y > 0):
            self.x = new_x
            self.y = new_y
        else:
            return not self.is_valid_move(new_x , new_y , board)
            
         
    def getMoves(self , position , board):
        #logic for moves
        return []
    def set_position(self , board):
        pass
    def get_position(self, board):
        ...
      
#creating a Pawn pievc extending the abstract class 
class Pawn(Piece):
    def __init__(self, color , x, y):
        super().__init__(color ,x ,y)
        
       

if  __name__== "__main__":
    
    piece = Piece()
    
    