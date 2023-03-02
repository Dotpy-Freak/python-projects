points = 0

try:
    print('Welcome to this quiz game.')
    user_interest = input('Do you want to start the game?(y/n): ')
    user_interest.lower()
    if user_interest == 'y':
        print("Ok! Let's start the game.")
        print('\n')

        answer = input('What does ISP stands for?: ')
        if answer.lower() == 'internet service provider':
            points += 1

        answer = input('What does EEPROM stands for?: ')
        if answer.lower() == 'electrically erasable programmable read only memory':
            points += 1

        answer = input('What does NAT stands for?: ')
        if answer.lower() == 'network address translation':
            points += 1

        answer = input('What does SRAM stands for?: ')
        if answer.lower() == 'static random access memory':
            points += 1

        answer = input('What does GPU stands for?: ')
        if answer.lower() == 'graphics processing unit':
            points += 1

        answer = input('What does CU stands for?: ')
        if answer.lower() == 'control unit':
            points += 1

        answer = input('What does ISP stands for?: ')
        if answer.lower() == 'internet service provider':
            points += 1

        answer = input('What does ISP stands for?: ')
        if answer.lower() == 'internet service provider':
            points += 1

        answer = input('What does ISP stands for?: ')
        if answer.lower() == 'internet service provider':
            points += 1

        answer = input('What does ISP stands for?: ')
        if answer.lower() == 'internet service provider':
            points += 1

    elif user_interest == 'n':
        quit()

except TypeError:
    print('Try some valid inputs!')

else:
    print('You successfully completed the quiz game.')


print()