'''
Created on 13.04.2015

@author: gereon
'''

class Language(object):
    '''
    classdocs
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
        
        
        
    Snippet

    def __init__(self, params):
        '''
        Constructor
        '''
        