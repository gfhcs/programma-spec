'''
Created on 14.04.2015

@author: gereon
'''

from LexPosition import LexPosition
from IdentifierToken import IdentifierToken
from LiteralToken import LiteralToken
from KeyWordToken import KeyWordToken
from CommentToken import CommentToken


class Lexer(object):
    '''
    Processes an iterable of binary code words and
    divides them into programming language tokens
    '''

    def __init__(self, language, codeWords, skipComments=True, newlineAsWhiteSpace=True):
        '''
        :param langauge: The language this lexer is supposed to work for
        :param codeWords: An iterable of code words to process
        '''
        
        self._lang = language
        self._source = iter(codeWords)
        self._newlineAsWhiteSpace = newlineAsWhiteSpace
        self._skipComments = skipComments
        self._pos = LexPosition()
        
        self._peekWord = None
        self._peekToken = None
        
        
        
    def matchKeyword(self, kw):
        if not isinstance(self.peek(), KeyWordToken):
            raise SyntaxError("Expected one of the following keywords: {kw}!".format(kw=kw), self._pos)
        
        if self.peek().getText() not in kw:
            raise SyntaxError("Expected one of the following keywords: {kw}!".format(kw=kw), self._pos)
        
        return self.read()
        
    def matchIdentifier(self):
        if not isinstance(self.peek(), IdentifierToken):
            raise SyntaxError("Expected identifier!", self._pos)
        
        return self.read()     
        
    def matchLiteral(self):
        if not isinstance(self.peek(), LiteralToken):
            raise SyntaxError("Expected literal!", self._pos)
        
        return self.read()
        
    def _peek(self):
        if self._peekWord is None:
            try:
                self._peekWord = self._source.__next__()
            except StopIteration:
                self._peekWord = None
            
        return self._peek
    
    def _read(self):
        w = self._peek()
        self._peekWord = None
        self._pos = self._pos.advance([w])
        return w
                
    def _isWhiteSpace(self, code):
        s = self._lang.getSpaceCode()
        n = self._lang.getNewlineCode()
        
        return code == s or (self._newlineAsWhiteSpace and code == n)
        
    def peek(self):
        
        if self._peekToken is None:
            
            state = None
            final = False
            prefix = ""
             
            while not final:
                lookahead = self._peek()
                for r in self._lang.getLexicalReductions():
                    if state != r.getCurrentTokenState():
                        continue
                    if not (r.getLookahead() == '?' or lookahead == r.getLookahead()):
                        continue
                    if (r.getMustSeeWhiteSpace() and not self._isWhiteSpace(lookahead)):
                        continue
                    if (r.getMustSeeKeyword() and lookahead[0] != '○'):
                        continue
                    if (r.getMustSeeIDSymbol() and lookahead[0] != '●'):
                        continue
                    
                    state = r.getNewTokenState()
                    if r.getEmpty():
                        prefix = ""
                    if r.getAppend():
                        prefix += lookahead
                    if r.getConsume():
                        self._read()
                    
                    final = r.getFinal()
                    break
            
            t = None
            
            if state is not None and final:
                if state == "kw":
                    t = KeyWordToken(self._lang, prefix)
                elif state == "id":
                    t = IdentifierToken(self._lang, prefix)
                elif state == "comment":
                    t = CommentToken(self._lang, prefix)
                    if self._skipComments:
                        t = self.peek()
                elif state == "bit":
                    t = LiteralToken(self._lang, prefix)
            else:
                if prefix == "":
                    t = None
                else:
                    raise SyntaxError("Lexical error!", self._pos)
                
            self._peekToken = t
            
        return self._peekToken
        
    def read(self):
        t = self.peek()
        self._peekToken = None
        return t
        