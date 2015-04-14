'''
Created on 13.04.2015

@author: gereon
'''

from Terminal import Terminal

class Keyword(Terminal):
    '''
    Represents a language keyword.
    '''
    
    def __eq__(self, other):
        return isinstance(other, Keyword) and self.getWord() == other.getWord()