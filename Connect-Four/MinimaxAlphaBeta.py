from main import *

MAX_DEPTH = 5  # Avoids the risk of Stack Overflow, 5 balances performance and decisions (I think)
win_conditions = winning_conditions()

def HeuristicEvaluations(board, player, computer, win_conditions):
    score = 0
    centre_col = 3
    
    '''Centre Priority'''
    centre_count = sum(1 for row in range(6) if board[centre_col][row] == computer)
    score += centre_count * 3
    
    
    for condition in win_conditions:
        player_count = sum(1 for row, col in condition if board[col][row] == player)
        computer_count = sum(1 for row, col in condition if board[col][row] == computer)
        
        if player_count > 0 and computer_count == 0:
            score -= 10 ** player_count  # Penalty for computer, encourages blocking winning moves from the human player
        elif computer_count > 0 and player_count == 0:
            score += 10 ** computer_count  # Reward for computer, encourages winning moves for the computer, exponents used to HIGHLY Penalise or Reward
    return score

def MinimaxAlphaBeta(board, depth, alpha, beta, MaximisingPlayer, player, computer, win_conditions):
    if (depth == 0 or 
        check_win(board, win_conditions, computer) or 
        check_win(board, win_conditions, player) or 
        all(board[col][0] != ' ' for col in range(7))):
        return HeuristicEvaluations(board, player, computer, win_conditions)
    '''If any condition is met, the function will return a heuristic score'''

    if MaximisingPlayer:
        MaxEval = float('-inf')
        for col in range(7):
            if board[col][0] == ' ':
                for row in reversed(range(6)):
                    if board[col][row] == ' ': # Finds empty cell
                        board[col][row] = computer # Places disc in empty cell
                        
                        eval = MinimaxAlphaBeta(board, depth-1, alpha, beta, False, player, computer, win_conditions) # Recursion
                        '''
                        - depth-1 makes algorithm reduce the depth each recursive call, allows to explore deeper
                        - alpha is best value that maximiser (computer) can currently guarantee
                        - beta is current best value that minimiser can guarantee
                        - False means its the minimsing player's turn (it flips each recursive call)
                        '''
                        
                        board[col][row] = ' '
                        MaxEval = max(MaxEval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:  # This Triggers Pruning
                            break
        return MaxEval
    
    else:
        MinEval = float('inf')
        for col in range(7):
            if board[col][0] == ' ':
                for row in reversed(range(6)):
                    if board[col][row] == ' ':
                        board[col][row] = player
                        
                        eval = MinimaxAlphaBeta(board, depth-1, alpha, beta, True, player, computer, win_conditions)
                        board[col][row] = ' '
                        MinEval = min(MinEval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
        return MinEval

def FindBestMove(board, player, computer):
    best_score = float('-inf')
    best_col = None
    
    for col in range(7):
        if board[col][0] == ' ':
            for row in reversed(range(6)):
                if board[col][row] == ' ':
                    board[col][row] = computer
                    score = MinimaxAlphaBeta(board, MAX_DEPTH, float('-inf'), float('inf'), False, player, computer, win_conditions)
                    board[col][row] = ' '
                    
                    if score > best_score:
                        best_score = score
                        best_col = col
                        
    return best_col
                    
                        
    
