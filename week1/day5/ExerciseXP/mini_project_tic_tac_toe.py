# What You’ll learn
# Conditionals (if, elif, else)
# Loops (for, while)
# Functions
# List manipulation
# User input


# Key Python Topics:

# Lists (2D lists)
# Loops (while)
# Conditional statements (if, elif, else)
# Functions
# User input (input())
# String formatting


# What you will create
# A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.

# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.

# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

# game_board = '''   |   |   
# ---|---|---
#    |   |   
# ---|---|---
#    |   |   '''
# print(game_board)
# # game_board_2D=game_board.split('\n')
# game_board_2D = list(list(row) for row in game_board.split('\n'))
# print(game_board_2D)

# col_count = len(game_board_2D[0])
# row_count = len(game_board_2D)

players_ind=(0,1)
players_symbol=('O','X')

# Step 2: Displaying the Game Board

# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

def display_board(board):
    for row in board:
        print(*row, sep="")

# display_board()

# Step 3: Getting Player Input

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

def player_input(player,board):

    valid_nr = ('1','2','3')
    active_step = True

    while active_step:
        # Row:
        while True:
            row_nr = input("Enter a valid row number 1,2,3 for your next step: ")
            if row_nr in valid_nr:
                # translate into actual row number in 2D dict board game:
                row_nr = 2 * int(row_nr) - 2 
                break
            else:
                print("The row number entered is invalid!")

        # Column:
        while True:
            col_nr = input("Enter a valid column number 1,2,3 for your next step: ")
            if col_nr in valid_nr:
                # translate into actual col number in 2D dict board game:
                col_nr = 4 * int(col_nr) - 3
                break
            else:
                print("The column number entered is invalid!")

        # Overall cell position:
        if board[row_nr][col_nr] == ' ':
            board[row_nr][col_nr] = players_symbol[player]
            print("Thank you, your step is performed")
            active_step = False
        else:
            print("This cell is already occupied, please choose another position!")

# Step 4: Checking for a Winner

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

winning_tuples = [
    # row wins:
    [(0,1),(0,5),(0,9)],[(2,1),(2,5),(2,9)],[(4,1),(4,5),(4,9)],
    # col wins:
    [(0,1),(2,1),(4,1)],[(0,5),(2,5),(4,5)],[(0,9),(2,9),(4,9)],
    # diagonal wins:
    [(0,1),(2,5),(4,9)],[(0,9),(2,5),(4,1)]
]

def check_win(board, player):

    # going through winning tuple lists and checking if at least one fully filled with play's symbol
    for win_pos in winning_tuples:
        i = 0
        while i < 3 and board[win_pos[i][0]][win_pos[i][1]] == players_symbol[player]:
            i += 1
        if i == 3:
            return True
        
    # otherwise no win:    
    return False

# Step 5: Checking for a Tie

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

def tie_check(board):

    # check whether all cells filled:
    for r in (1,2,3):
        for c in (1,2,3):
            if board[2*r-2][4*c-3] == ' ':
                # one empty found -> not a tie:
                return False
    
    # otherwise, if all not empty, check by player if one won:
    for player in players_ind: # (0,1)
        if check_win(board, player) == True:
            return False # i.e. no tie
        
    # otherwise all filled and no winner -> tie = True:
    return True

# Step 6: The Main Game Loop

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def play():
    # initialize the game board:
    game_board = '''   |   |   
---|---|---
   |   |   
---|---|---
   |   |   '''
    game_board_2D = list(list(row) for row in game_board.split('\n'))
    i = 0

    # while no tier and no win by anyone (all false -> sum = 0):
    while True:
        display_board(game_board_2D)
        print(f"Player {i}, your turn to put an {players_symbol[i]}.")
        # player i -> get input and update
        player_input(players_ind[i],game_board_2D)

        if check_win(game_board_2D, players_ind[i]) == True:
            result = 'Game: the winner is player ' + str(i) + '!'
            break
        # next player's turn:
        if tie_check(game_board_2D) == True:
            result = "It's a tie!"
            break
        i = abs(i-1) # If 1->0, if 0->1
    print(result)
    display_board(game_board_2D)

play()
