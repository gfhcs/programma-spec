'''
Created on 13.04.2015

@author: gereon
'''

from NonTerminal import NonTerminal
from GrammarExpression import GrammarExpression

class Production(object):
    '''
    Represents a production rule in a context-free grammar (CFG).
    '''

    def __init__(self, name, rhs):
        '''
        Creates a new syntactic grammar production rule
        '''
        self._name = name
        self._rhs = rhs
                
    def getName(self):
        return self._name
    
    def getRightHandSide(self):
        return self._rhs
            
    def __str__(self):
        return "{nt} ::= {rhs}".format(nt=self._name, rhs=self._rhs)
    
    @staticmethod
    def parse(source):
        
        name = NonTerminal.parse(source).getName()
        
        source.match("::=")
        
        rhs = GrammarExpression.parse(source)
        
        if source.peek() == ".":
            source.read()
        
        return Production(name, rhs)
        
    def getTerminals(self):
        return self._rhs.getTerminals()
    
    def getNonTerminals(self):
        return self._rhs.getNonTerminals()
