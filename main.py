# imports
from time import gmtime, strftime
from cliff.logging import *

# variables
username = 'user'
hostname = 'host'

# main
while True:
    prefix_time = strftime('%H:%M:%S', gmtime())
    cmd = input(cyan('┌──(') + blue(username + '@' + hostname) + cyan('- [') + magenta(prefix_time) + cyan(']') + cyan('\n└─') + blue('$ '))

    if cmd == 'help':
        print('Useful help text')

    elif cmd == '' or cmd.startswith(' '):
        continue
    
    elif cmd == 'aaa':
        print('@@@ test AAAA')

    else:
        err('The command \"' + cmd + '\" you are trying to access is unknown.')