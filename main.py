from tictactoe import TicTacToe
import random

def main():
    """ create an instance of TicTacToe class"""
    t = TicTacToe()
        
    #get the value of whose turn it is X or O
    board_state = random.choice([t.STATES.NAUGHT_TURN, t.STATES.CROSS_TURN])

    """ use a while loop to intrectively play TicTacToe and save the board state
        run loop until someone wins or its draw
        get the valid user input for location in form of row,col
        call place_marker funtion on user input and print the updated board state 
    """
    while board_state != t.STATES.NAUGHT_WON and board_state != t.STATES.CROSS_WON and board_state != t.STATES.DRAW:
        print(board_state)
        val = input('Enter location in format row,column:').split(',')
        turn = 'x' if (board_state == t.STATES.CROSS_TURN) else 'o'
        row = int(val[0]) 
        col = int(val[1])

        if row not in range(0,3) or col not in range(0,3) or t.board[row][col] != ' ':
            print('Please enter valid location in format row,column')
            continue
    
        board_state = t.place_marker(turn,row,col) 
        print(t.board[0])
        print(t.board[1])
        print(t.board[2])
    print(board_state)

if __name__ == "__main__":
    main()