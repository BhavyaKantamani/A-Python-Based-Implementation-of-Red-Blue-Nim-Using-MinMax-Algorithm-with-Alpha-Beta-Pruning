Name: Bhavya Sri Kantamani
UTA ID: 1002118109

Programming Language Used:
--------------------------
Python
Version: 3.8.5

Code Structure:
---------------
1. `state_bxk`: Global variable to maintain the current game state (number of red and blue marbles).
2. `bxk_minmax`: Implements the MinMax algorithm with Alpha-Beta pruning and depth limitation.
3. `bxk_eval_game_state`: Evaluates the game state, providing a score based on the current state and the game's version (standard or misère).
4. `bxk_get_possible_moves`: Generates all possible moves from the current game state, considering the game's rules.
5. `bxk_make_move`: Applies a given move to the game state, updating the state accordingly.
6. `bxk_human_move`: Handles human player input, validating and applying the move.
7. `bxk_game_over`: Checks if the game has reached an end condition based on the current state.
8. `bxk_display_final_score`: Calculates and displays the final score once the game is over, based on the remaining marbles.
9. `bxk_main`: The main function that initiates and controls the game flow based on user inputs and the MinMax algorithm.

How to Run the Code:
--------------------
No compilation is needed as the script is written in Python. To run the game, use the following command in a terminal:

```
python red_blue_nim.py <num-red> <num-blue> [<version> <first-player> <depth>]
```

- `<num-red>`: Number of red marbles at the start of the game.
- `<num-blue>`: Number of blue marbles at the start of the game.
- `<version>`: Game version, either `standard` or `misere`. Optional, defaults to `standard`.
- `<first-player>`: Who starts the game, either `computer` or `human`. Optional, defaults to `computer`.
- `<depth>`: Depth limit for the MinMax search. Optional, not required unless implementing depth-limited search.

Example:
```
python red_blue_nim.py 8 8 standard computer 10
```

ACS Omega Compatibility:
------------------------
This code is designed to be run in a standard Python environment and has not been specifically tested on the ACS Omega system. Ensure Python 3.8.5 or a compatible version is installed on the system where the code will be executed.