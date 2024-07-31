
def is_over(board_status: list[list[int]]):
    """
    board_status: list[list[int]]
    This function will check is the game is over, meaning all fields have been marked
    Returns True (False) if game is over (is not over)
    """
    for row in board_status[:]:
        for i in row:
            if i == 0:
                return False
    return True

def game_result(board_status: list[list[int]], winner, playerA_score, playerB_score):
    """
    board_status: list[list[int]]
    This function will check if someone won or if there is a tie
    Return which player won or it its a tie
    """
    player_A = 1
    player_B = -1
    #check rows and columns for winner
    for i in range(3):
        if board_status[i][0] == board_status[i][1] == board_status[i][2] == player_A:
            return [player_A, playerA_score+1, playerB_score]
        elif board_status[0][i] == board_status[1][i] == board_status[2][i] == player_A:
            return [player_A, playerA_score+1, playerB_score]
        elif board_status[i][0] == board_status[i][1] == board_status[i][2] == player_B:
            return [player_B, playerA_score, playerB_score+1]
        elif board_status[0][i] == board_status[1][i] == board_status[2][i] == player_B:
            return [player_B, playerA_score, playerB_score+1]
    
    #check diagonals for winner
    if board_status[0][0] == board_status[1][1] == board_status[2][2] == player_A:
        return [player_A, playerA_score+1, playerB_score]
    elif board_status[2][0] == board_status[1][1] == board_status[0][2] == player_A:
        return [player_A, playerA_score+1, playerB_score]
    elif board_status[0][0] == board_status[1][1] == board_status[2][2] == player_B:
        return [player_B, playerA_score, playerB_score+1]
    elif board_status[2][0] == board_status[1][1] == board_status[0][2] == player_B:
        return [player_B, playerA_score, playerB_score+1]
    
    if is_over(board_status):
        return [0, playerA_score, playerB_score]    #nobody won, its a tie
    else:
        return [winner, playerA_score, playerB_score]
    