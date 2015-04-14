'''
Created on 13.04.2015

@author: gereon
'''

from GrammarExpression import GrammarExpression

class Epsilon(GrammarExpression):
    '''
    Represents the empty word.
    '''

    def __str__(self):
        return "ε"
    
    def __eq__(self, other):
        return isinstance(other, Epsilon)
    
    def __hash__(self):
        return 0
    
    @staticmethod
    def parse(source):
        source.match("ε")
        return Epsilon()
    
    def getTerminals(self):
        return iter([])
    
    def getNonTerminals(self):
        return iter([])
