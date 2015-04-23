'''
Created on 20.04.2015

@author: gereon
'''

from Token import Token
from util.util import *

class CommentToken(Token):
    '''
    Represents a comment as found in the source code.
    '''

    def __init__(self, language, code, position):
        '''
        Creates a new identifier token
        '''
        
        super(self, CommentToken).__init__(position)
        
        comment = ""
        
        rcw = language.getCodeWidth() - 1
        
        for b in ichunks(islice(code, -rcw, 1), rcw):
            comment += chr(bin2int(b))
        
        self._comment = comment
        
    def getComment(self):
        return self._comment