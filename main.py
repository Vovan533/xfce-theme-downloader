import sys
import os
from termcolor import colored, cprint
import config


# start
print(config.LOGO)
print('Made with ' + colored('<3', 'magenta') + ' ' + config.AUTHOR)
print('version: ' + config.VERSION)


# update
def update():
    print('\n' + colored('Updating...', 'magenta') + '\n')
    print('Removing previous version...')
    os.chdir(os.path.dirname(os.getcwd()))
    os.system('rm -rf S1MpL3B00Mb3r')
    print('Install new version from github...')
    os.system('git clone ' + config.GITHUB)
    print('\n' + colored(':D', 'yellow') + '\nUpdate finished, restart programm')
    exit()


# loop
txt = '\nSelect feature >>\n' + colored('01', 'cyan') + colored(' - ', 'grey') + colored('SMS bomber', 'cyan') + "\n" + colored('02', 'yellow') + colored(' - ', 'grey') + colored('Email bomber', 'yellow') + "\n" + colored('03', 'green') + colored(' - ', 'grey') + colored('WhatsApp bomber', 'green') + "\n" + colored('00', 'magenta') + colored(' - ', 'grey') + colored('Update', 'magenta') + "\n" + colored('99', 'red') + colored(' - ', 'grey') + colored('Exit', 'red') + '\n\n'
while True:
    inp = input(txt)
    if inp == '99':
        print(colored('\nBye', 'blue') + '!')
        exit()
    elif inp == '00' or inp == '0':
        print(0)
    elif inp == '01' or inp == '1':
        print(1)
    elif inp == '02' or inp == '2':
        print('\n' + colored(':(', 'red') + '\nFuture not avaliable yet')
    elif inp == '03' or inp == '3':
        print('\n' + colored(':(', 'red') + '\nFuture not avaliable yet')
    else:
        print('\n' + colored(':/', 'red') + '\nInvalid input')