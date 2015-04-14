'''
Created on 13.04.2015

@author: gereon
'''

class Language(object):
    '''
    Represents a programming language.
    '''
    
    def __init__(self, grammar=None, categories=[]):
        self._grammar = grammar
        self._categories = categories
        
    def getCategories(self):
        return iter(self._categories)
    
    def setCategories(self, categories):
        self._categories = categories
    
    def getConcreteGrammar(self):
        return self._grammar

    def setConcreteGrammar(self, g):
        self._grammar = g

    def generateLexicalSpec(self):
    
    def generateLexer(self):
        
    def generateParser(self):
        