from tictactoe import TicTacToe
    
def main():
    """ create an instance of TicTacToe class"""
    t = TicTacToe()
        
    #get the value of whose turn it is
    board_state = t.cur_state

    """ use a while loop to intrectively play TicTacToe and save the board state
        run loop until someone wins or its draw
        get the valid user input for location in form of row,col
        call place_marker funtion on user input and print the updated board state 
    """
    while board_state != t.STATES.NAUGHT_WON and board_state != t.STATES.CROSS_WON and board_state != t.STATES.DRAW:

        val = input('Enter location in format row,column:').split(',')
        turn = 'x' if (board_state == t.STATES.CROSS_TURN) else 'o'
        row = int(val[0]) 
        col = int(val[1])

        if row not in range(0,3) or col not in range(0,3) or t.board[row][col] != ' ':
            val = input('Please enter valid location in format row,column:').split(',')
            row = int(val[0]) 
            col = int(val[1])
    
        #print(turn,row,col)
        board_state = t.place_marker(turn,row,col) 
        print(board_state)
        print(t.board[0])
        print(t.board[1])
        print(t.board[2])

if __name__ == "__main__":
    main()