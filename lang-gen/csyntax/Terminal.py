'''
Created on 13.04.2015

@author: gereon
'''

from GrammarExpression import GrammarExpression

class Terminal(GrammarExpression):
    '''
    Represents a syntactic terminal symbol.
    '''

    def __init__(self, word):
        super(self, Terminal).__init()
        self._word = word

    def __str__(self):
        return self._word
    
    def __eq__(self, other):
        return isinstance(other, Terminal) and other._word == self._word
    
    def __hash__(self):
        return hash(self._word)
    
    def getWord(self):
        return self._word
    
    @staticmethod
    def parse(source):
        if source.delimits(source.peek()):
            raise Exception("Expected a terminal symbol, but found '{f}'!".format(f=source.peek()))
        
        w = source.read().trim('"')
        
        from Keyword import Keyword
        
        return Terminal(w) if len(w) == 1 else Keyword(w)
    
    def getTerminals(self):
        return iter([self])
    
    def getNonTerminals(self):
        return iter([])

    
