# reference board position
print('1 | 2 | 3')
print('4 | 5 | 6')
print('7 | 8 | 9' + '\n')

board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

# !!!!!!Global Variable!!!!!!!!!
game_still_going = True
current_player = 'X'
winner = None


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():

    # display the initial board
    display_board()

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        check_if_game_ended()

        swap_player()

        # the game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')

    else:
        print('Its a tie!')


def check_if_game_ended():
    check_for_winner()
    check_for_tie()


def check_for_winner():

    global winner # Setting winner a global variable

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there is no win
        winner = None
    return


def check_rows():
    # setting up a global variable
    global game_still_going
    # check if any of the rows have all the same value ( and is not empty )
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'
    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner ( X or O )
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # setting up a global variable
    global game_still_going
    # check if any of the columns have all the same value ( and is not empty )
    col_1 = board[0] == board[3] == board[6] != '_'
    col_2 = board[1] == board[4] == board[7] != '_'
    col_3 = board[2] == board[5] == board[8] != '_'
    # if any row does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False

    # return the winner ( X or O)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    # setting up a global variable
    global game_still_going
    # check if any of the diagonals have all the same value ( and is not empty )
    diagonal_1 = board[0] == board[4] == board[8] != '_'
    diagonal_2 = board[2] == board[4] == board[6] != '_'

    # if any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner ( X or O )
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_for_tie():
    global game_still_going

    if '_' not in board:
        game_still_going = False
    return


def swap_player():

    global current_player
    # fi the current player was x then change it to 'O' and vice versa
    if current_player == 'X':
        current_player = 'O'
    elif current_player == "O":
        current_player = 'X'

    return


def handle_turn(current_player):

    print(current_player + "'s turn.")
    position = input('Choose a position from 1 - 9: ')

    valid = False

    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Invalid input. Please choose a position from 1 - 9: ')

        position = int(position) - 1

        if board[position] != '_':
            print('That space is already used up. Please try some other place.')
        else:
            valid = True

    board[position] = current_player
    display_board()


play_game()
