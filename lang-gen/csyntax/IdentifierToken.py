'''
Created on 20.04.2015

@author: gereon
'''

from Token import Token
from util.util import *

class IdentifierToken(Token):
    '''
    Represents an identifier as found in the source code.
    '''

    def __init__(self, language, code, position):
        '''
        Creates a new identifier token
        '''
        
        super(self, IdentifierToken).__init__(position)
        
        name = ""
        rcw = language.getCodeWidth() - 1
        
        for b in ichunks(islice(code, -rcw, 1), rcw):
            name += chr(bin2int(b))
        
        self._name = name
        
    def getName(self):
        return self._name