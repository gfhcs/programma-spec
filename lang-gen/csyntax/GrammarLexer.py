'''
Created on 13.04.2015

@author: gereon
'''

from io import TextIOBase

class GrammarLexer(object):
    '''
    A tokenizer for Backus-Naur-Form grammars
    '''

    def __init__(self, source):
        '''
        Creates a new GrammarLexer
        :param source: The source character stream
        '''

        if not isinstance(source, TextIOBase):
            raise Exception("The given source must be a TextIOBase object!")

        self._peekC = None
        self._peekT = None
        self._source = source

    def _peekChar(self):
        
        if self._peekC is None:
            self._peekC = self._source.read(1)
            
            if self._peekC == "":
                raise Exception("No input remaining!")
            
        return self._peek()
        
        
    def _readChar(self):
        c = self._peekChar()
        self._peekC = None
        return c


    def _skipWhiteSpace(self):
        while self._peekChar().isspace():
            self._readChar()
        
        
    def match(self, m):
        if self.peek() != m:
            raise Exception("Found {f} instead of {e}!".format(f=self.peek(), e=m))

        self.read()
        
    def read(self):
        r = self.peek()
        self._peekT = None
        return r
        
        
    def eos(self):
        try:
            self.peek()
            return False
        except:
            return True 
    
    def delimits(self, c):
        return (c in "ε<>|().\"") or c.isspace()
        
    def peek(self):
        
        if self._peekT is None:
            self._skipWhiteSpace()
                    
            c = self._readChar()
            self._peekT = c
            
            if c == '"':
                
                
                while self._peekChar() != '"':
                    
                    c = self._readChar()
                    
                    if c == '\\' and self._peekChar() == '"':
                        self._readChar()
                        c = '"'
                    
                    self._peekT += c
            
                self._peekT += self._readChar()

            elif not self.delimits(c):
            
                while not self.delimits(self._peekChar()):
                    self._peekT += self._readChar()
            
        
        return self._peekT
    