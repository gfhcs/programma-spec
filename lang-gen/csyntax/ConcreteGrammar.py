'''
Created on 14.04.2015

@author: gereon
'''

from Keyword import Keyword
from Production import Production

from util.util import int2bin

import math

class ConcreteGrammar(object):
    '''
    A set of production rules that constitute the concrete semantics of a programming language.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._lexicalReductions = []
        self._lexicalCategories = []
        
        self._productions = {}
        self._terminals = set([])
        self._keywords = set([])
        
        self._cachesValid = True
        self._sealed = False
        
    def addLexicalReduction(self, r):
        
        if self._sealed:
            raise Exception("This grammar has been sealed and cannot be modified anymore!")
        
        self._lexicalReductions.append(r)
        self._cache_lexical(r)
        
        
    def removeLexicalReduction(self, r):
        
        if self._sealed:
            raise Exception("This grammar has been sealed and cannot be modified anymore!")
        
        self._lexicalReductions.remove(r)
        self._cachesValid = False

        
    def addProduction(self, p):
        if self._sealed:
            raise Exception("This grammar has been sealed and cannot be modified anymore!")
        
        if p.getName() in self._productions:
            raise Exception("There already is another production for the non-terminal symbol '{nt}'".format(nt=p.getName()))
        
        self._productions[p.getName()] = p
        self._cache_phrasal(p)
    
    def isSealed(self):
        return self._sealed
    
    def seal(self):        
        for p in self._productions.itervalues():
            for nt in p.getNonTerminals():
                try:
                    nt.setDefinition(self._productions[nt.getName()])
                except KeyError:
                    nt.setToToken()

        self._computeBinaryMap()

        self._sealed = True
    
    
    def _computeBinaryMap(self):
        
        self._symbols = set([" ", "\n"])
        
        for lr in self._lexicalReductions:
            
            s = lr.getLookAhead()
            
            if s is not None and s != "?":
                self._symbols.add(s)
                
        for kw in self._keywords:
            self._symbols.add(kw)
    
        self._lexWordLength = int(math.ceil(math.log(len(self._symbols), 2))) + 1
        
        i = 0
        for s in self._symbols:
            self._binMap[s] = int2bin(i)
            i += 1
        
    def getBinaryMap(self):
        return self._binMap
    
    def getBinaryWordLength(self):
        return self._lexWordLength
    
    def _cache_lexical(self, reduction):
        if reduction.getFinal():
            self._lexicalCategories.append(reduction.getNewTokenState())
    
    def _cache_phrasal(self, production):
        t = production.getTerminals()
        self._terminals |= t
        self._keywords |= filter(t, lambda t : isinstance(t, Keyword))
    
    def _cache_all(self, production):
        
        if not self._cachesValid:
        
            self._lexicalCategories.clear()
            
            for r in self._lexicalReductions:
                self._cache_lexical(r)
        
            self._terminals.clear()
            self._keywords.clear()
            
            for p in self._productions:
                self._cache_phrasal(p)
        
        self._cachesValid = True
        
    def removeProduction(self, p):
        
        if self._sealed:
            raise Exception("This grammar has been sealed and cannot be modified anymore!")
        
        self._productions.remove(p)
        self._cachesValid = False
        
    def getLexicalCategories(self):
        return iter(self._lexicalCategories)    
    
    def getLexicalReductions(self):
        return iter(self._lexicalReductions)
    
    def getProductions(self):
        return iter(self._productions)
    
    def getTerminals(self):
        self._cache_all()
        return iter(self._terminals)
    
    def getKeywords(self):
        self._cache_all()
        return iter(self._keywords)
    
    def parsePhrasalGrammar(self, source):
        while not source.eos():
            self.addProduction(Production.parse(source))
            
    def __str__(self):
        s = ""
        prefix = ""
        
        for p in self._productions:
            s += prefix + str(p)
            prefix = ".\n"
            
        return s
        
        