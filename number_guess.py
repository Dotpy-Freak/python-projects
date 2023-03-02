import random

user_range = int(input('Enter the range till where the secret number will be: '))
print('#' * 250)

def guess(user_range):
        random_number = random.randint(1, user_range)
        users_input = 0

        while users_input != random_number:
            try:

                #print('\n')
                print('#' * 250)

                users_input = int(input(f"Guess a number between 1 and {user_range}: "))

                if users_input < random_number:

                    #print('\n')
                    print('#' * 250)
                    print('Ah! The number is greater than the one you guessed.')

                elif users_input > random_number:

                    #print('\n')
                    print('#' * 250)
                    print('C\'mon\', the number is lesser than you think.')
            except:
                #print('\n')
                print('#' * 250)
                print('Don\'t\' try anything else except number!')


        #print('\n')
        print('#' * 250)

        print('Congratulations! You guessed it correctly.')


guess(user_range)







