from GamePieces import Pawn , Bishop , King
import sys
#Changes

def create_board():
    columns = '  A B C D E F G H'
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],  # 8
        ["p"] * 8,                                # 7
        [" "] * 8,                                # 6
        [" "] * 8,                                # 5
        [" "] * 8,                                # 4
        [" "] * 8,                                # 3
        ["P"] * 8,                                # 2
        ["R", "N", "B", "Q", "K", "B", "N", "R"]   # 1
    ]

    print(columns)
    for row in range(8):
        line = f"{8 - row} "
        for col in range(8):
            piece = board[row][col]
            square_color = "⬛" if (row + col) % 2 == 0 else "⬜"
            if piece != " ":
                line += piece + " "
            else:
                line += square_color + " "
        print(line)
    print(columns)
   
   
def game_loop():
    board = create_board()  
    #creating Pieces
    white_pawn = Pawn("white", 4 , 1)
    black_paw =  Pawn("black",4 , 6 )
    white_pawn.set_position(board)
    black_paw.set_position(board)
    players = ["white","black"]
               
    turn = 0
    
    while True:
        current_color = players[turn % 2]
        print(board)
        print(f"{current_color}'s turn")
        
        
        
        move= input("Enter move (x1 y1 x2 y2) or 'q' to quit:)").strip()
        if move.lower() == 'q':
            print("Game ended")
            sys.exit
            break
        
        try:
             x1, y1, x2, y2  = map(int ,move.split())
        except ValueError:
           print("Invalid input")
           continue
       
       
        piece =board[y1][x1]
       
       
        if piece is None:
           print("No piece at that position")
            
        if piece.color != current_color:
            print("That is not your piece")
            continue
        
        
        
def main():
    #Game loop 
    pass
    
    
    
if __name__=="__main__":
    main()
