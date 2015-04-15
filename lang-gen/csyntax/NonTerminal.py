'''
Created on 13.04.2015

@author: gereon
'''

from GrammarExpression import GrammarExpression

class NonTerminal(GrammarExpression):
    '''
    Represents a non-terminal symbol, i.e. a reference to a production rule.
    '''

    def __init__(self, name):
        self._name = name
        self._production = None
        self._isToken = False

    def __str__(self):
        return "<{n}>".format(n=self._name)
    
    def __eq__(self, other):
        return isinstance(other, NonTerminal) and other.getName() == self.getName()
    
    def __hash__(self):
        return hash(self._name)
    
    def getName(self):
        return self._name
    
    def getProductionRule(self):
        return self._production
    
    def setProductionRule(self, p):
        
        if self._production is not None:
            raise Exception ("This non-terminal has already been bound to a production rule!")
        
        if self._name != p.getName():
            raise Exception ("The nonterminal {s} cannot be bound to the production rule {r}, because names don't match!".format(s=self, r=p))
        
        self._production = p
        
    def setToToken(self):
        if self._production is not None:
            raise Exception ("This non-terminal has already been bound to a production rule!")
        
        self._isToken = True
        
    def isToken(self):
        return self._isToken
    
    @staticmethod
    def parse(source):
        
        source.match("<")
        
        if source.delimits(source.peek()):
            raise Exception("Expected a non-terminal name, but found '{f}'!".format(f=source.peek()))
        
        n = source.read()
        
        source.match(">")
        
        return NonTerminal(n)
    
    def getTerminals(self):
        return iter([])
    
    def getNonTerminals(self):
        return iter([self])
