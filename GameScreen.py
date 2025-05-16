import pygame
import GamePieces

# Screen
class Screen:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.medium_font = pygame.font.Font('freesansbold.ttf', 40)
        self.big_font = pygame.font.Font('freesansbold.ttf', 50)
        self.timer = pygame.time.Clock()
        self.fps = 60
        self.screen = None

    def viewScreen(self, width, height):
        self.screen = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Two player chess game")

    def draw_Pieces_into_board(self):
        for i in range(len(GamePieces.white_pieces)):
            index = GamePieces.piece_list.index(GamePieces.white_pieces[i])
            if GamePieces.white_pieces[i] == "pawn":
                self.screen.blit(
                    GamePieces.white_pawn,
                    (
                        GamePieces.white_locations[i][0] * 100 + 22,
                        GamePieces.white_locations[i][1] * 100 + 22
                    )
                )
            else:
                self.screen.blit(
                    GamePieces.white_images[index],
                    (
                        GamePieces.white_locations[i][0] * 100 + 10,
                        GamePieces.white_locations[i][1] * 100 + 10
                    )
                )

            if GamePieces.turn_step < 2 and GamePieces.selection == i:
                pygame.draw.rect(
                    self.screen,
                    'red',
                    [
                        GamePieces.white_locations[i][0] * 100 + 1,
                        GamePieces.white_locations[i][1] * 100 + 1,
                        100, 100
                    ],
                    2
                )

    def draw_board(self, width, height):
        for i in range(32):
            column = i % 4
            row = i // 4

            if row % 2 == 0:
                pygame.draw.rect(
                    self.screen,
                    "light gray",
                    [600 - (column * 200), row * 100, 100, 100]
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    'light gray',
                    [700 - (column * 200), row * 100, 100, 100]
                )

        pygame.draw.rect(self.screen, "gray", [0, 800, width, 100])
        pygame.draw.rect(self.screen, 'gray', [0, 800, width, 100])
        pygame.draw.rect(self.screen, 'gold', [0, 800, width, 100], 5)
        pygame.draw.rect(self.screen, 'gold', [800, 0, 200, height], 5)

        status_text = [
            'White: Select a Piece to Move!',
            'White: Select a Destination!',
            'Black: Select a Piece to Move!',
            'Black: Select a Destination!'
        ]

        self.screen.blit(
            self.big_font.render(
                status_text[GamePieces.turn_step], True, 'black'
            ),
            (20, 820)
        )


if __name__ == "__main__":
    screen = Screen()
    screen.viewScreen(1000, 900)
