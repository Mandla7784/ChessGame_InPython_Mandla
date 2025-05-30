from GamePieces import Pawn, Bishop, King
from Board import Board


import pygame
import sys


#TODO : Adding music background 

def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load("chess.mp3")
    pygame.mixer.music.set_volume(0.2) 
    pygame.mixer.music.play(-1)
    
def stop_music():
        pygame.mixer.music.pause() 
    
# Game loop
def game_loop():
    board =   Board.create_board()

    # Creating Pieces
    white_pawn = Pawn("white", 4, 6)
    black_pawn = Pawn("black", 4, 1)

    board[6][4] = white_pawn  # Replace character with object
    board[1][4] = black_pawn

    white_pawn.set_position(board)
    black_pawn.set_position(board)

    players = ["white", "black"]
    turn = 0

    while True:
        current_color = players[turn % 2]
        start_music()

        print(f"\n{current_color}'s turn")
        move = input("Enter move (x1 y1 x2 y2) or 'q' to quit: ").strip()
        if move.lower() == 'q':
            print("Game ended.")
            stop_music()
            sys.exit() #exiting the systems
            break

        try:
            x1, y1, x2, y2 = map(int, move.split())
        except ValueError:
            print("Invalid input format.")
            continue

        try:
            piece = board[y1][x1]
        except IndexError:
            print("Invalid board position.")
            continue

        if piece == " " or piece is None:
            print("No piece at that position.")
            continue

        if not hasattr(piece, "color") or piece.color != current_color:
            print("That is not your piece.")
            continue

        if piece.is_valid_move(x2, y2, board):
            if piece.get_name() == "pawn" and y2 < y1 and piece.color == "white":
                print("White pawn cannot move backward.")
                continue
            if piece.get_name() == "pawn" and y2 > y1 and piece.color == "black":
                print("Black pawn cannot move backward.")
                continue

            board[y1][x1] = " "
            board[y2][x2] = piece
            piece.set_moves(x2, y2, board)
            turn += 1
        else:
            print("Invalid move. Try again.")

# Main function
def main():
    game_loop()  

if __name__ == "__main__":
    main()
