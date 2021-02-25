import unittest
from typing import List
from tictactoe import TicTacToe

class TicTacToeTest(unittest.TestCase):
    
    def test_cross_won(self):
        t = TicTacToe()

        self.assertEqual(t.place_marker('x',0,0),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',2,2),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',2,0),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',1,2),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',0,2),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',2,2),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',1,1),t.STATES.CROSS_WON)
   
    def test_naught_won(self):
        t = TicTacToe()
        self.assertEqual(t.place_marker('o',2,2),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',0,0),t.STATES.NAUGHT_TURN) 
        self.assertEqual(t.place_marker('o',0,2),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',1,1),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',1,2),t.STATES.NAUGHT_WON)

    def test_draw(self):
        t = TicTacToe()
        self.assertEqual(t.place_marker('o',0,0),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',0,2),t.STATES.NAUGHT_TURN) 
        self.assertEqual(t.place_marker('o',0,1),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',1,0),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',1,1),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',2,2),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',2,0),t.STATES.CROSS_TURN)
        self.assertEqual(t.place_marker('x',2,1),t.STATES.NAUGHT_TURN)
        self.assertEqual(t.place_marker('o',1,2),t.STATES.DRAW)
   
    def test_row(self):
        t = TicTacToe()
        board: List[List[str]] = [['x', 'o', 'x'],['o', 'x', 'x'],['o', 'x', 'x']]
        self.assertTrue(t.row_checker(board) == (False,))
        board = [['x', 'o', ' '],['x', 'x', 'x'],['o', 'o', 'x']]
        self.assertTrue(t.row_checker(board) == (True,'x'))

    def test_col(self):
        t = TicTacToe()
        board: List[List[str]] = [['x', 'o', 'x'],['o', 'x', 'x'],['o', 'x', 'x']]
        self.assertTrue(t.col_checker(board) == (True,'x'))
        board = [['x', 'o', 'x'],['o', 'x', 'x'],[' ', ' ', ' ']]
        self.assertTrue(t.col_checker(board) == (False,)),

    def test_dgn_rl(self):
        t = TicTacToe()
        board: List[List[str]] = [['x', 'o', 'x'],['o', 'x', 'x'],['o', 'x', 'x']]
        self.assertTrue(t.dgn_rl_checker(board) == (False,))
        board = [['x', 'o', 'x'],['o', 'x', 'x'],['x', ' ', ' ']]

    def test_dgn_lr(self):
        t = TicTacToe()
        board: List[List[str]] = [['x', 'o', 'x'],['o', 'x', 'x'],['o', 'x', 'x']]
        self.assertTrue(t.dgn_lr_checker(board) == (True,'x'))
        board = [[' ', 'o', 'x'],['o', 'x', 'x'],['o', 'x', 'x']]
        self.assertTrue(t.dgn_lr_checker(board) == (False,))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

