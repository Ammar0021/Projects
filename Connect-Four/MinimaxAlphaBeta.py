from main import *


def MinimaxAlphaBeta(board, depth, alpha, beta, MaximisingPlayer, player, computer):
    win_conditions = winning_conditions
    
    if check_win(board, win_conditions, computer):
        return 100 - depth # Makes the Algorithm find quicker wins
    if check_win(board, win_conditions, player):
        return 100 - depth # Makes algorithm avoid Quicker losses
    if all(board[col][0] != ' ' for col in range(7)):
        return 0 # Draw
    
    if MaximisingPlayer:
        MaxEval = float('-inf')
        for col in range(7):
            if board[col][0] == ' ':
                for row in reversed(range(6)):
                    if board[col][row] == ' ': # Finds empty cell
                        board[col][row] = computer # Places disc in empty cell
                        
                        eval = MinimaxAlphaBeta(board, depth-1, alpha, beta, True, player, computer) # Recursive Call
                        '''depth-1 makes algorithm reduce the depth each recursive call
                        alpha is best value that maximiser (computer) can currently guarantee, (beta is opposite)
                        True means move is being made by maximiser (computer)'''
                        
                        
    
