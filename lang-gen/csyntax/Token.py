'''
Created on 20.04.2015

@author: gereon
'''

class Token(object):
    '''
    Represents a lexical token as found in the source code.
    '''

    def __init__(self, position):
        '''
        Creates a new token
        '''
        self._pos = position

    def getPosition(self):
        return self._pos