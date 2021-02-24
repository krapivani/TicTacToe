from enum import Enum
import random

class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    
    def __init__(self):
        """creat a blank board of size 3X3 """
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        """ randomly select whose turn it is o or x """
        self.cur_state = random.choice([self.STATES.NAUGHT_TURN, self.STATES.CROSS_TURN])

    def place_marker(self, symbol, row, column):
        """assing the given symbol to board with given row,column
            and use different function to determine what STATE and return the STATE
        """
        self.board[row][column] = symbol

        row_check = self.row_checker(self.board)
        if row_check[0]:
            if row_check[1] == 'x': 
                return self.STATES.CROSS_WON
            else:
                return self.STATES.NAUGHT_WON
        
        col_check = self.col_checker(self.board)
        if col_check[0]:
            if col_check[1] == 'x':
                return self.STATES.CROSS_WON
            else:
                return self.STATES.NAUGHT_WON

        dgn_rl_check = self.dgn_rl_checker(self.board)
        if dgn_rl_check[0]:
            if dgn_rl_check[1] == 'x':
                return self.STATES.CROSS_WON
            else:
                return self.STATES.NAUGHT_WON
        
        dgn_lr_check = self.dgn_lr_checker(self.board)
        if dgn_lr_check[0]:
            if dgn_lr_check[1] == 'x':
                return self.STATES.CROSS_WON
            else:
                return self.STATES.NAUGHT_WON
        
        if self.is_draw(self.board):
            return self.STATES.DRAW

        if symbol == 'x':
            return self.STATES.NAUGHT_TURN
        else:
            return self.STATES.CROSS_TURN

    def row_checker(self,board):
        """ check rows if there is a winning combination 
            and return True and the winner if there is winning combination
        """
        for i in range(len(board)):
            for j in range(1, len(board)):
                if board[i][0] != board[i][j] or board[i][0] == ' ':
                    break
            else:
                return (True,board[i][0])
        return(False,)


    def col_checker(self,board):
        """ check columns if there is a winning combination
            and return True and the winner if there is winning combination
         """
        for i in range(len(board)):
            for j in range(1, len(board)):
                if board[0][i] != board[j][i] or board[0][i] == ' ':
                    break
            else:
                return (True,board[0][i])
        return(False,)


    def dgn_lr_checker(self,board):
        """ check diagonal left to right if there is a winning combination 
            and return True and the winner if there is winning combination
        """
        for i in range(0, len(board)):
            if board[0][0] != board[i][i] or board[0][i] == ' ':
                break
        else:
            return (True,board[0][0])
        return(False,)
        

    def dgn_rl_checker(self,board):
        """ check diagonal right to left if there is a winning combination 
            and return True and the winner if there is winning combination
        """
        for i, j in zip(range(0, len(board)), reversed(range(0, len(board)))):
            if board[0][len(board)-1] != board[i][j] or board[0][len(board)-1] == ' ':
                break
        else:
            return (True,board[0][len(board)-1])
        return(False,)
    
    def is_draw(self,board):
        """ check the board to see if it is draw condition """
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    return False
        return True


   
    
        