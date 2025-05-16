import pygame


#Screen
class Screen:
    def __init__(self):
        pass



    def viewScreen( width ,height):
        screen = pygame.display.set_mode([width  , height])
        pygame.display.set_caption("Two player chess game")
        font = pygame.font.Font('freesansbold.ttf', 20)
        medium_font = pygame.font.Font('freesansbold.ttf', 40)
        big_font = pygame.font.Font('freesansbold.ttf', 50)
        timer = pygame.time.Clock()
        fps = 60
        
    def draw_board():
        for i in range(32):
            column = i % 4
            row = i  // 4
            
            if row  % 2 == 0:
                pygame.draw.rect(self , "light gray" , [
                    
                    600 - (column * 200), row * 100, 100, 100
                    
                ])
            else:
                 pygame.draw.rect(self, 'light gray', [

                             700 - (column * 200), row * 100, 100, 100])

        