from cliff.general import *
from cliff.logging import *

commands = {
    'help': 'help()',
    '': '',
    ' ': ''
}

while True:
     cmd = input('>> ')
     
     if cmd in commands:
          exec(commands[cmd])
     else:
          err('no')