import unittest
from main import  create_board


class Test_Main(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        
        
    def test_create_board(self):
        self.assertEqual( create_board(),
  """
                           A B C D E F G H
                            8 r n b q k b n r 
                            7 p p p p p p p p 
                            6 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
                            5 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
                            4 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
                            3 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
                            2 P P P P P P P P 
                            1 R N B Q K B N R 
                            A B C D E F G H
                                                    
                         
                         """)
    
if __name__=="__main__":
    unittest.main()
    