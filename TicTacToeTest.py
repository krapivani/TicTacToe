import unittest
from typing import List
from tictactoe import TicTacToe

class TicTacToeTest(unittest.TestCase):
    
    def test_checkers(self):
        t = TicTacToe()
       
        """ testing row, column and diagonal checkers """
        
        self.assertEqual(t.place_marker('x',0,0),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',2,2),t.STATES.CROSS_TURN)


        board: List[List[str]] = [['x', 'o', 'x'],
                                  ['o', 'x', 'x'],
                                  ['o', 'x', 'x']]
        
        self.assertTrue(t.row_checker(board) == (False,))
        self.assertTrue(t.col_checker(board) == (True,'x'))
        self.assertTrue(t.dgn_lr_checker(board) == (True,'x'))
        self.assertTrue(t.dgn_rl_checker(board) == (False,))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

