'''
Created on 13.04.2015

@author: gereon
'''

from GrammarExpression import GrammarExpression
from Epsilon import Epsilon
from NonTerminal import NonTerminal
from Choice import Choice
from Terminal import Terminal
import itertools

def _flatten(components):
    newComponents = []
    
    for c in components:
        if isinstance(c, Concatenation):
            newComponents.extend(_flatten(c.getComponentsIter()))
        else:
            newComponents.append(c)
            
    return newComponents
    

class Concatenation(GrammarExpression):
    '''
    Represents a grammatical concatenation of word sets.
    '''

    def __init__(self, components):
        self._components = _flatten(components)

    def __str__(self):
        
        s = ""
        p = ""
        
        for c in self._components:
            
            d = str(c)
            
            if isinstance(c, Choice):
                d = "({d})".format(d=d)
            
            s += p + d
            p = " "
            
        return s
    
    def __eq__(self, other):
        if not isinstance(other, Concatenation):
            return False
        
        for (a, b) in itertools.izip(self._components, other._components):
            if a != b:
                return False
            
        return True
    
    def __hash__(self):
        h = 0
        for c in self._components:
            h += c
        return h
    
    def getComponentsIter(self):
        return iter(self._components)
    
    def _parsePrimitive(self, source):
        
        f = source.peek()
        
        if f == "ε":
            return Epsilon.parse(source)
        elif f == "<":
            return NonTerminal.parse(source)
        elif f == "(":
            source.read()
            e = GrammarExpression.parse(source)
            source.match(")")
            return e
        else:
            return Terminal.parse(source)
    
    @staticmethod
    def parse(source):
        
        c = [Concatenation._parsePrimitive(source)]
        
        while source.peek() not in  ".|":
            c.append(Concatenation._parsePrimitive(source))
        
        if len(c) == 1:
            return c[0]
        
        return Concatenation(c)