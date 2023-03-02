import random

try:

    def computer_guess(x):
        low = 1
        high = x
        feedback = ""
        tries = 1

        while feedback != 'c':
             guess = random.randint(low, high)

             feedback = str(input(f'Is {guess} too high (H), too low (L) or correct (C)?')).lower()

             if feedback == 'h':
                 high = guess - 1
                 tries += 1

             elif feedback == 'l':
                 low = guess + 1
                 tries += 1
        print('\n')
        print(f'Oh! The number that you guessed was {guess} which the computer guessed after {tries} tries.')

    computer_guess(12)

except:

    print('Please enter either H, L or C only!')