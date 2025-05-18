import pygame
pygame.init()

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
    
def print_board():
    create_board()
        
      
def main():
    print_board()
    
if __name__=="__main__":
    main()
