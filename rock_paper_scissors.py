import random


def play():
    user = input("""  'r' for rock
  'p' for paper
  's' for scissor
-->""")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie.'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    if is_win(computer, user):
        return 'You lost! Better luck next time. '


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's' ) or (player == 'p' and opponent == 'r' ) \
            or (player == 's' and opponent == 'p'):
        return True
    else:
        print('Please use a valid command!')


go_forward = 0
while go_forward != 1:

    start = input('Enter play to start the game - ')
    start.lower()
    if start == 'play':
        go_forward = 1
        print(play())
    else:
        print('Invalid commands won\'t start the game.')
        print('\n')