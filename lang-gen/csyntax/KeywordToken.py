'''
Created on 20.04.2015

@author: gereon
'''

from Token import Token

class KeywordToken(Token):
    '''
    Represents a key word as found in the source code.
    '''

    def __init__(self, language, code, position):
        '''
        Creates a new keyword token
        '''
        
        super(self, KeywordToken).__init__(position)
        
        self._code = code
        self._text = language.getBinaryMap()[code]

        
    def getCode(self):
        return self._code
    
    def getText(self):
        return self._text