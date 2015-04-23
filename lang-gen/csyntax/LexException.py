'''
Created on 22.04.2015

@author: gereon
'''

class LexException(Exception):
    '''
    Represents a lexical failure
    '''

    def __init__(self, msg):
        super(self, LexException).__init__(msg)