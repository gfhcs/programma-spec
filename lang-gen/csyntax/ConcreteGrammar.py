'''
Created on 14.04.2015

@author: gereon
'''

from Keyword import Keyword
from Production import Production

class ConcreteGrammar(object):
    '''
    A set of production rules that constitute the concrete semantics of a programming language.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._productions = {}
        self._terminals = set([])
        self._keywords = set([])
        
        self._cachesValid = True
        self._sealed = False
        
    def addProduction(self, p):
        if self._sealed:
            raise Exception("This grammar has been sealed and cannot be modified anymore!")
        
        if p.getName() in self._productions:
            raise Exception("There already is another production for the non-terminal symbol '{nt}'".format(nt=p.getName()))
        
        self._productions[p.getName()] = p     
        self._cache_single(p)
    
    def isSealed(self):
        return self._sealed
    
    def seal(self):        
        for p in self._productions.itervalues():
            for nt in p.getNonTerminals():                
                nt.setProduction(self._productions[nt.getName()])

        self._sealed = True
    
    def _cache_single(self, production):
        t = production.getTerminals()
        self._terminals |= t
        self._keywords |= filter(t, lambda t : isinstance(t, Keyword))
    
    def _cache_all(self, production):
        
        if not self._cachesValid:
        
            self._terminals.clear()
            self._keywords.clear()
            
            for p in self._productions:
                self._cache_single(p)
        
        self._cachesValid = True
        
    def removeProduction(self, p):
        
        if self._sealed:
            raise Exception("This grammar has been sealed and cannot be modified anymore!")
        
        self._productions.remove(p)
        self._cachesValid = False
        
    def getProductions(self):
        return iter(self._productions)
    
    def getTerminals(self):
        self._cache_all()
        return iter(self._terminals)
    
    def getKeywords(self):
        self._cache_all()
        return iter(self._keywords)
    
    @staticmethod
    def parse(source):
        
        g = ConcreteGrammar()
        
        while not source.eos():
            g.addProduction(Production.parse(source))
        
        g.seal()
        
        return g
        
        