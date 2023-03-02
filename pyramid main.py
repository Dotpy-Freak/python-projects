

spacex = ' '
# Validation of max symbols.
def val_max_sym():

    sym = 2
    while sym % 2 == 0:
        print('Enter the max number of symbols. ')
        sym = int(input(': '))

    return sym


# calling the val_max function
max_symb = val_max_sym()


# setting the values required for setting the values of the pyramid

print('Enter your preferred symbol.')
symbol = input(": ")
no_spaces = int((max_symb - 1) / 2)
no_of_sym = 1

# running the loop until number of symbols is lesser than max_symbols
while max_symb >= no_of_sym:

    # to output the spaces and print the symbols
    print(spacex * no_spaces, symbol * no_of_sym)


    # print('\n')  # moving to a new line

    # adjusting no_of spaces !!!

    no_spaces -= 1

    # adjusting no of symbols to be printed

    no_of_sym += 2




