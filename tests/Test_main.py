import unittest
from main import  create_board  , start_music , stop_music
from unittest.mock import patch


import pygame

class Test_Main(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
       
    def test_create_board(self):
        self.assertEqual( create_board(),
  """
                             A  B  C  D  E  F  G  H
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 
6 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
5 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
4 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
3 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 
  A  B  C  D  E  F  G  H
                                                    
                         
                         """)
        
        
        
@patch("pygame.mixer.music.play")
@patch("pygame.mixer.music.set_volume")
@patch("pygame.mixer.music.load")
@patch("pygame.mixer.init")
def  test_startMusic(self ,  mock_init, mock_load, mock_set_volume, mock_play):
    start_music()
    mock_init.assert_called_once()
    mock_load.assert_called_once_with("chess.mp3")
    mock_set_volume.assert_called_once_with(0.2)
    mock_play.assert_called_once_with(-1)
     
    
@patch("pygame.mixer.music.pause")

def test_stop_music(self , mock_pause):
    stop_music()
    mock_pause.asssert_called_once()
    
    
    
if __name__=="__main__":
    unittest.main()
    