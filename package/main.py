import pygame
pygame.init()


def create_board():
    board = [
        ["w","h","i","t","ePieces"],
        [" "] * 8,
      ["r", "n", "b", "q", "k", "b", "n", "r"],  # Black pieces
        ["p"] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        ["P"] * 8,
        ["R", "N", "B", "Q", "K", "B", "N", "R"],  # White pieces  
        [" "] * 8,
        ["B","l","a","c","k","p","i","e","c","es"]
    ]
    
    return board

def print_board(board):

    for row in board: # looping on each row and print the data
        print(" ".join(row))
        
      
def main():
    board = create_board()
    print_board(board=board)

    
if __name__=="__main__":
    main()
