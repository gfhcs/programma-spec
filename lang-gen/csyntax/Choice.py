'''
Created on 13.04.2015

@author: gereon
'''

from GrammarExpression import GrammarExpression

def _flatten(alternatives):
    newAlternatives = []
    
    for a in alternatives:
        if isinstance(a, Choice):
            newAlternatives.extend(_flatten(a.getAlternativesIter()))
        else:
            newAlternatives.append(a)
            
    return newAlternatives

class Choice(GrammarExpression):
    '''
    Represents a grammatical concatenation of word sets.
    '''

    def __init__(self, alternatives):
        super(self, Choice).__init()
        self._alternatives = _flatten(alternatives)

    def __str__(self):
        
        s = ""
        p = ""
        
        for c in self._alternatives:
            s += p + str(c)
            p = " | "
            
        return s
    
    def __eq__(self, other):
        if not isinstance(other, Choice):
            return False
        
        oa = set(other._alternatives)
        
        try:            
            for a in self._alternatives:
                oa.pop(a)
        except KeyError:
            return False
            
        return len(oa) == 0
    
    def __hash__(self):
        h = 0
        for c in self._alternatives:
            h += c
        return h
    
    def getAlternativesIter(self):
        return iter(self._alternatives)
    
    @staticmethod
    def parse(source):
        
        from Concatenation import Concatenation
        
        a = [Concatenation.parse(source)]
        
        while source.peek() != ".":
            a.append(Concatenation._parsePrimitive(source))
        
        if len(a) == 1:
            return a[0]
        
        return Choice(a)
    
    def getTerminals(self):
        for a in self._alternatives:
            for t in a.getTerminals():
                yield t
    
    def getNonTerminals(self):
        for a in self._alternatives:
            for nt in a.getNonTerminals():
                yield nt
