import pygame

# Initialize parameters
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# Check whether the game is still going or not
still_going = True

winner = None

# X always goes first
current_player = 'X'


# Print out the board
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


# Start the game
def play_game():
    print_board()

    while still_going:
        # Players fill in a certain position into the board
        handle_turn(current_player)
        # Check whether the game's over or not
        check_if_game_over()
        # Switch turns
        flip_turn()

    if winner == 'X' or winner == 'O':
        print(winner + ' wins')
    elif winner == 'None':
        print('Tie')


def check_if_game_over():
    # Check if a player wins
    check_if_win()
    # Check if the match is tie
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_rows()
    col_winner = check_cols()
    diag_winner = check_diag()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None


# Check rows for a win
def check_rows():
    global still_going

    # All values in one of the rows must be the same in order to win ('-' doesn't count)
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    # Stop the game when we have a winner
    if row1 or row2 or row3:
        still_going = False

    # Return the winner ('X' or 'O')
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


# Check columns for a win
def check_cols():
    global still_going

    # All values in one of the columns must be the same in order to win ('-' doesn't count)
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    # Stop the game when we have a winner
    if col1 or col2 or col3:
        still_going = False

    # Return the winner ('X' or 'O')
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None


# Check diagonals for a win
def check_diag():
    global still_going

    # All values in one of the diagonals must be the same in order to win ('-' doesn't count)
    diag1 = board[0] == board[4] == board[8] != '-'
    diag2 = board[2] == board[4] == board[6] != '-'

    # Stop the game when we have a winner
    if diag1 or diag2:
        still_going = False

    # Return the winner ('X' or 'O')
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    else:
        return None


def check_if_tie():
    global still_going

    if '-' not in board:
        still_going = False
        return True
    else:
        return False


# Switch players' turn
def flip_turn():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


# Players input a number
def handle_turn(player):
    print(player + '\'s turn')

    valid = False
    while not valid:
        position = int(input('Type in a number from 1 to 9: '))
        while position not in range(1, 10, 1):
            position = int(input('Type in a number from 1 to 9: '))
        position = position - 1
        if board[position] == '-':
            board[position] = player
            print_board()
            valid = True
        else:
            print('Occupied. Go again!')


print('Welcome to Tic Tac Toe')
play_game()

