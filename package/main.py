from GamePieces import Pawn, Bishop, King
import sys

# Create the board and display it
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

    return board  # RETURN the board so it's usable in game_loop()

# Game loop
def game_loop():
    board = create_board()

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

        print(f"\n{current_color}'s turn")
        move = input("Enter move (x1 y1 x2 y2) or 'q' to quit: ").strip()
        if move.lower() == 'q':
            print("Game ended.")
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
