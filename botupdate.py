import os
import config.py
from sys import argv

''' Handling test '''
if len(argv) > 1:
    if argv[1] == 'test':
        print('Imports successful!')
        exit(0)
        

""" Handling the PORT for deployment """

PORT = int(os.environ.get('PORT', 5000))
