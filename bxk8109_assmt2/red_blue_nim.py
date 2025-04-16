import sys

# Global state of the game
state_bxk = [0, 0]

def bxk_minmax(state, depth, alpha, beta, maximizingPlayer, version_bxk, depth_limit_bxk):
    """
    Implements the MinMax algorithm with Alpha-Beta pruning and depth limitation.
    """
    if depth == depth_limit_bxk or bxk_game_over(state, version_bxk):
        return bxk_eval_game_state(state, version_bxk, depth, maximizingPlayer, depth_limit_bxk), None

    moves = bxk_get_possible_moves(state, version_bxk)

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for move in moves:
            newState = bxk_make_move(state, move)
            evaluation, _ = bxk_minmax(newState, depth+1, alpha, beta, False, version_bxk, depth_limit_bxk)
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in moves:
            newState = bxk_make_move(state, move)
            evaluation, _ = bxk_minmax(newState, depth+1, alpha, beta, True, version_bxk, depth_limit_bxk)
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return minEval, best_move

def bxk_eval_game_state(state, version_bxk, depth, maximizingPlayer, depth_limit_bxk):
    """
    Evaluates the game state with nuanced strategies for standard and misère versions,
    adjusting based on the depth to favor quicker wins or longer defenses.
    """
    if version_bxk == 'standard':
        score = (state[0] * 2) + (state[1] * 3)
        depth_factor = depth_limit_bxk - depth
    else:
        score = -((state[0] * 2) + (state[1] * 3))
        depth_factor = depth

    if maximizingPlayer:
        return score + depth_factor
    else:
        return score - depth_factor

def bxk_get_possible_moves(state, version_bxk):
    """
    Generates possible moves from the current state, adjusts order based on game version.
    """
    moves = []
    if version_bxk == 'standard':
        order = [(2, 'red'), (2, 'blue'), (1, 'red'), (1, 'blue')]
    else:
        order = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]
    
    for num, color in order:
        if (color == 'red' and state[0] >= num) or (color == 'blue' and state[1] >= num):
            moves.append((color, num))
    return moves

def bxk_make_move(state, move):
    """
    Applies a move to the game state and returns the new state.
    """
    newState = state.copy()
    if move[0] == 'red':
        newState[0] -= move[1]
    else:
        newState[1] -= move[1]
    return newState

def bxk_human_move():
    """
    Gets and validates the human player's move.
    """
    global state_bxk
    while True:
        pile = input("Choose a pile (red or blue): ").strip().lower()
        num = input("Choose the number of marbles to remove (1 or 2): ").strip()
        
        if pile in ['red', 'blue'] and num.isdigit() and int(num) in [1, 2]:
            num = int(num)
            if (pile == 'red' and state_bxk[0] >= num) or (pile == 'blue' and state_bxk[1] >= num):
                return (pile, num)
        
        print("Invalid move. Please try again.")

def bxk_game_over(state, version_bxk):
    """
    Checks if the game is over based on the state and version.
    """
    return state[0] <= 0 or state[1] <= 0

def bxk_display_final_score(state, version_bxk, first_player_bxk):
    """
    Calculates and displays the final score based on remaining marbles.
    Adjusts the message based on the game version and the player who made the last move.
    """
    score = (state[0] * 2) + (state[1] * 3)
    game_ended_on_computer_turn = first_player_bxk == 'human'
    
    if version_bxk == 'standard':
        if game_ended_on_computer_turn:
            print(f"Computer loses with a final score of {score} points. Human wins!")
        else:
            print(f"Human loses with a final score of {score} points. Computer wins!")
    else:
        if game_ended_on_computer_turn:
            print(f"Computer wins with a final score of {score} points. Human loses!")
        else:
            print(f"Human wins with a final score of {score} points. Computer loses!")

def bxk_main():
    global state_bxk

    # Validate the number of command-line arguments
    if len(sys.argv) < 3 or len(sys.argv) > 6:
        print("Usage: red_blue_nim.py <num-red> <num-blue> [<version> <first-player> <depth>]")
        sys.exit(1)
    
    # Validate that the number of red and blue marbles are integers
    try:
        num_red_bxk, num_blue_bxk = int(sys.argv[1]), int(sys.argv[2])
    except ValueError:
        print("Error: The number of red and blue marbles must be integers.")
        sys.exit(1)
    
    # Validate the version
    version_bxk = 'standard' if len(sys.argv) < 4 else sys.argv[3]
    if version_bxk not in ['standard', 'misere']:
        print("Error: <version> must be 'standard' or 'misere'.")
        sys.exit(1)

    # Validate the first player
    first_player_bxk = 'computer' if len(sys.argv) < 5 else sys.argv[4]
    if first_player_bxk not in ['computer', 'human']:
        print("Error: <first-player> must be 'computer' or 'human'.")
        sys.exit(1)

    # Set the depth limit with a default of 5
    depth_limit_bxk = 5 if len(sys.argv) < 6 else int(sys.argv[5])

    # Initialize the game state
    state_bxk = [num_red_bxk, num_blue_bxk]

    while not bxk_game_over(state_bxk, version_bxk):
        if first_player_bxk == 'computer':
            _, move = bxk_minmax(state_bxk, 0, float('-inf'), float('inf'), True, version_bxk, depth_limit_bxk)
            if move:
                state_bxk = bxk_make_move(state_bxk, move)
                print(f"Computer plays: {move[1]} {move[0]} marbles")
            first_player_bxk = 'human'
        else:
            move = bxk_human_move()
            state_bxk = bxk_make_move(state_bxk, move)
            print(f"You play: {move[1]} {move[0]} marbles")
            first_player_bxk = 'computer'
        
        if bxk_game_over(state_bxk, version_bxk):
            print("Game over!")
            bxk_display_final_score(state_bxk, version_bxk, first_player_bxk)

if __name__ == "__main__":
    bxk_main()