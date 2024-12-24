from main import *

MAX_DEPTH = 7  # Avoids the risk of Stack Overflow, 7 balances performance and decisions (I think)

def MinimaxAlphaBeta(board, depth, alpha, beta, MaximisingPlayer, player, computer):
    if depth <= 0:
        return 0
    
    win_conditions = winning_conditions()
    
    if check_win(board, win_conditions, computer):
        return 100 - depth # Encourages the Algorithm find quicker wins
    if check_win(board, win_conditions, player):
        return 100 - depth # Encourages algorithm avoid moves leading to loss
    if all(board[col][0] != ' ' for col in range(7) for row in range(6)):
        return 0 # Draw
    
    if MaximisingPlayer:
        MaxEval = float('-inf')
        for col in range(7):
            if board[col][0] == ' ':
                for row in reversed(range(6)):
                    if board[col][row] == ' ': # Finds empty cell
                        board[col][row] = computer # Places disc in empty cell
                        
                        eval = MinimaxAlphaBeta(board, depth-1, alpha, beta, not MaximisingPlayer, player, computer) # Recursion
                        '''
                        - depth-1 makes algorithm reduce the depth each recursive call, allows to explore deeper
                        - alpha is best value that maximiser (computer) can currently guarantee
                        - beta is current best value that minimiser can guarantee
                        - not MaximisingPlayer flips the current turn
                        '''
                        
                        MaxEval = max(MaxEval, eval)
                        alpha = max(alpha, eval)
                        
                        if beta <= alpha: # Triggers pruning
                            break
                        board[col][row] = ' '
        return MaxEval
    
    else:
        MinEval = float('inf')
        for col in range(7):
            if board[col][0] == ' ':
                for row in reversed(range(6)):
                    if board[col][row] == ' ':
                        board[col][row] = player
                        
                        eval = MinimaxAlphaBeta(board, depth-1, alpha, beta, not MaximisingPlayer, player, computer)
                        MinEval = min(MinEval, eval)
                        beta = min(beta, eval)
                        
                        if beta <= alpha:
                            break
                        board[col][row] = ' '
        return MinEval
    
                        
    
