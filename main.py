# imports
from time import gmtime, strftime
from cliff import *

# variables
username = 'user'
hostname = 'host'

# main
while True:
    prefix_time = strftime('%H:%M:%S', gmtime())
    cmd = input(cyan('┌──(') + blue(username + '@' + hostname) + cyan('- [') + magenta(prefix_time) + cyan(']') + cyan('\n└─') + blue('$ '))

    if cmd == 'help':
        help()

    elif cmd == '' or cmd.startswith(' '):
        continue
    
    elif cmd == 'cls' or cmd == 'clear':
        clear()

    else:
        err('The command \"' + cmd + '\" you are trying to access is unknown.')