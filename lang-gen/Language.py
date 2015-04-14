'''
Created on 13.04.2015

@author: gereon
'''

class Language(object):
    '''
    Represents a programming language.
    '''
    
    dumpLexerSpec
    dumpParserSpec
    
    dumpLexer
    dumpParser
    
    
    ConcreteGrammar
    
        attach(Snippet)
    
        Production
        
            attach(Snippet)
        
            Label
            Right-Hand-Side
                Concatenation
                Alternative
                Terminal
                Epsilon
    
            AbstractCorrespondence
    
    
    AbstractGrammar
        
        attach(Snippet)
    
        Name
        Constituents
        ConcreteCorrespondence
        
    def dump(self, target, output):
        
        if target == self._target:
            output.write(self._content)
            
    def dumpLexerSpec(self, output):
        
        
            
            
    def __init__(self, params):
        '''
        Constructor
        '''
        