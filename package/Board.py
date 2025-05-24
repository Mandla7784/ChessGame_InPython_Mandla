""""
 TODO: 
 Proper method definition (self) and class usage.

Use Unicode chess pieces for a visual appeal.

Align the board properly so it doesn’t look jagged.

Retain the square color pattern when empty.


"""

class Board:

    # Create the board and display it
    def create_board(self):
        
            
        columns = '  A  B  C  D  E  F  G  H'
        board = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
]

        
        
        print(columns)
        for row in range(8):
            line = f"{8 - row} "
            for col in range(8):
                piece = self.board[row][col]
                square_color = "⬛" if (row + col) % 2 == 0 else "⬜"
                line += f"{piece if piece != ' ' else square_color} "
            print(line)
        print(columns)
        return  board  # RETURN the board so it's usable in game_loop()
