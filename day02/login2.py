import getpass

username = input('Plase input your username: ')
password = getpass.getpass('Password: ')
if username == 'casey' and password == 'hello':
    print('Login Successful!\nWelcome {}'.format(username))
else:
    print('Username or password not correct. Please input again.')
