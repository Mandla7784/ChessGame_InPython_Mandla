""""
 TODO: 
 Proper method definition (self) and class usage.

Use Unicode chess pieces for a visual appeal.

Align the board properly so it doesn’t look jagged.

Retain the square color pattern when empty.


"""

class Board:
    def __init__(self):
        self.columns = '  A  B  C  D  E  F  G  H'
        self.board = [
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],  # 8
            ["♟"] * 8,                                # 7
            [" "] * 8,                                # 6
            [" "] * 8,                                # 5
            [" "] * 8,                                # 4
            [" "] * 8,                                # 3
            ["♙"] * 8,                                # 2
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]   # 1
        ]
    

        # Create the board and display it
    def create_board():
      
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


        return board  # RETURN the board so it's usable in game_loop()