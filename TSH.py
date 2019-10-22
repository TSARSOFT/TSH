# TSARSOFT TSH

import os

dir='~/'
prompt='TSH('+dir+')->'

_help='\ncommands:\nhelp\ncd\nls\n<shell command>'

def cmd():
    global dir
    global prompt
    cmd=input(prompt)
    if str(cmd.split()[0])=='cd':
        dir=cmd.split()[1]
    elif str(cmd.split()[0])=='ls':
        os.system('ls '+dir)
    elif str(cmd.split()[0])=='help':
        print(_help)
    else:
        os.system(cmd)
    prompt='TSH('+dir+')->'

if os.path.isfile('TSHRC'):
    exec(open('TSHRC', 'r').read())
else:
    print('TSHRC file not found')

while True:
    cmd()
