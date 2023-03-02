# importing the time module
import time

# welcoming the user

name = input('What is your name? ')

print(f'Hello,{name}. Time to play hangman!')

print("")


# wait for 1 second

time.sleep(1)
print("Start guessing...")

time.sleep(0.5)

# the secret word
secret_word = "valorant"

# creates an variable with an empty value
guesses = ""

turns = 10

# hint

print("""        Its a popular pc game. 
        Online 5 v 5.
        Try guessing it!
        
        
        _ _ l _ _ _ _ _""")

# creates an while loop

while turns > 0:
    #asking the user
    guess = input('Enter a word: ')

    # make a counter that starts with zero
    failed = 0
    user_guess = guess.lower()
    # for every character in secret_word
    '''for char in secret_word:
        guesses = guesses + char'''

    # see if the character is in the players guess
    # if char in guess:

            # print then out the character
        # print(char)

    '''else:

            # if not found then print a dash
        print("_")

            # deducts the turns for every error
        turns -=1'''

    if user_guess == secret_word:
        print(f'Congratulations! {name} you have guessed it correctly.')

    else:
        print('Try again.')
        turns -=1




