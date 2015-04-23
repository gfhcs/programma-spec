'''
Created on 20.04.2015

@author: gereon
'''

from Token import Token
from util.util import *

class LiteralToken(Token):
    '''
    Represents a comment as found in the source code.
    '''

    def __init__(self, language, code, position):
        '''
        Creates a new identifier token
        '''
        
        super(self, LiteralToken).__init__(position)
        
        literal = ""
        for b in ichunks(code, language.getCodeWidth()):
            literal += language.getBinaryMap()[b]
        
        self._literal = literal
        
    def getLiteral(self):
        return self._literal