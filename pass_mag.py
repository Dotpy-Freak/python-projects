from cryptography.fernet import Fernet


def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
    return key


master_pwd = input('Enter the master password: ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print(f'User: {user}')
            print('Password: ' + fer.decrypt(passw.encode()).decode() + '\n')


def add():
    usr_name = input('Enter the user name: ')
    pwd = input('Enter the password: ')
    with open('password.txt', 'a') as f:
        f.write(usr_name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    print('Enter either view or add. Press q to quit')
    mode = input('Enter the mode: ').lower()

    if mode == 'q':
        quit()

    if mode == 'view':
        view()

    elif mode == 'add':
        add()

    else:
        print('Invalid mode. Try again.')
        continue
