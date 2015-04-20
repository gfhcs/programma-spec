'''
Created on 20.04.2015

@author: gereon
'''

from util.util import int2bin

class Text2Binary(object):
    '''
    Converts an iterable of unicode characters into an iterable of binary code words for a given proramming language.
    '''

    def __init__(self, language, text):
        '''
        :param language: The language for which to create the Text2Binary object
        :param text: The unicode iterable to convert.
        '''
        self._lang = language
        
        self._chars = iter(text)
        
        self._pc = None
        self._insideComment = False
        
        self._buffer = []
        
    def __iter__(self):
        return self
    
    def _peek(self):
        
        if self._pc is None:
            self._pc = self._chars.__next__()
            
        return self._pc
        
    def _read(self):
        c = self._peek()
        self._pc = None
        return c
    
    def _convertKeyWord(self, kw):
        return self._lang.getConcreteGrammar().getBinaryMap()[kw]
        
    def _convertFree(self, text):
        
        wl = self._lang.getConcreteGrammar().getBinaryWordLength()
        
        binary = ""
        
        for c in text:
            binary += int2bin(c)
            while len(binary) >= wl:
                self._buffer.append(binary[:wl])
                binary = binary[wl:]
        
        while len(binary) >= wl:
            self._buffer.append(binary[:wl])
            binary = binary[wl:]
        
        if len(binary) > 0:    
            while len(binary) < wl:
                binary += '○'
            self._buffer.append(binary)
        
    def _convertLiteral(self, literal):
        for c in literal:
            self._buffer.append(self._lang.getConcreteGrammar().getBinaryMap()[c])
        
    
    def __next__(self):
        
        if len(self._buffer) > 0:
            return buffer.pop()
        
        c = self._peek()
        w = ""
        
        if self._insideComment:
            while c != "#":
                w += c
                self._read()
                c = self._peek()
        
            return self._convertFree(w)
        
        elif c == "\n":
            self._read()            
            return self._convertKeyWord(c)            
        elif c.isspace():
            self._read()            
            return self._convertKeyWord(" ")            
        elif c == "#":
            self._read()
            self._insideComment = not self._insideComment
            return self._convertKeyWord(c)
        elif c in ["●○"]:
            while c in ["●○"]:
                w += c
                self._read()
                c = self._peek()
            return self._convertLiteral(w)
        else:
            while (len(w) == 0 or c not in self._lang.getConcreteGrammar().getBinaryMap()) and not c.isspace():
                w += c
                self._read()
                c = self._peek()
            
            if w in self._lang.getConcreteGrammar().getBinaryMap():
                return self._convertKeyWord(w)
            else:
                return self._convertFree(w)
            