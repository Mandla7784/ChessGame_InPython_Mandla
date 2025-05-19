from abc import ABC,abstractmethod


#Abstract class 
class Piece(ABC):
    def __init__(self,color , x ,y):
        self.color = color 
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{self.color} {self.__class__.__name__} at ({self.x} , {self.y} )"
    
    
    #check valid move on a piece 
    @abstractmethod
    def is_valid_move(self , new_x , new_y  ,board):
        pass
    
        

     #setting a new position of a piece on board 
    @abstractmethod  
    def set_moves(self, new_x, new_y , board):
      pass
  
  
    @abstractmethod
    def get_moves(self , board):
     pass

    
    
    @abstractmethod
    def set_position(self , board):
        pass
    @abstractmethod
    
    def get_position(self, board):
        ...
      
#creating a Pawn pievc extending the abstract class 
class Pawn(Piece):
    def __init__(self, color , x, y):
        super().__init__(color ,x ,y)
        
    def is_valid_move(self , new_x , new_y  ,board):
        
        if self.color == "white":
            if new_x == self.x and new_y == self.y+1 and board[new_x][new_y] is None:
                return True
            
    
        if not (0 <= new_x < len(board) and 0 <= new_y < len(board)):
            return False
        return True
    
    
    def set_moves(self, new_x, new_y , board):
        
        if(new_x > 0 and new_y > 0):
            self.x = new_x
            self.y = new_y
        else:
            return not self.is_valid_move(new_x , new_y , board)
        
    def set_position(self, board):
       board[self.y][self.x] = self
       
       
    def get_position(self):
        return self.x , self.y
    
    
        
    def get_moves(self,board):
        moves = []
        direction = 1 if self.color == "white" else  -1
        new_x = self.x
        new_y = self.y
        new_y  = self.y + direction
        
        if 0 <= new_y < len(board) and board[new_y][new_x] is None:
            moves.append((new_x, new_y))
            
        return moves
class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        
        
        
class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        
        
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        
       
         
if  __name__== "__main__":
    
    board = [[None for _ in range(8)] for _ in range(8)]
    
    pawn = Pawn("white", 4, 1)
    print(pawn)  # white Pawn at (4, 1)
    
    pawn.set_position(board)
    
    print("Valid Moves:", pawn.get_moves( board))
    
    if pawn.set_moves(4, 2, board):
        print("Moved to:", pawn.get_position(board))
    else:
        print("Invalid move")