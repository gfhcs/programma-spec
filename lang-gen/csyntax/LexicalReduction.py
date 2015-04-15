'''
Created on 15.04.2015

@author: gereon
'''

class LexicalReduction(object):
    '''
    Represents a 'lexical reduction': A lexical reduction is a mathematical rule specifying
    how the lexer, given a certain lexical state (a triple of token state, token prefix and input rest), transitions to the
    next state.
    '''

    def __init__(self, (currentTokenState, lookahead), (newTokenState, empty, append, consume, final), (mustSeeWhiteSpace, mustSeeKeyWord, mustSeeIDSymbol)=(False, False, False)):
        '''
        Creates a new lexical reduction.
        :param currentTokenState: A string identifying the token type that is currently being lexed. Use None if no token type has been chosen yet.
        :param lookahead: The symbol the lexer is looking at. Use '?' for any and None for the end of input.
        :param newTokenState: A string identifying the token type is being lexed after the transition. Use None if no token type has been chosen yet.
        :param empty: A boolean value specifying whether the token prefix is to be cleared (before appending the lookahead character).
        :param append: A boolean value specifying whether the lookahead character is to be append to the current token.
        :param consume: A boolean value specifying whether the lookahead character is to be consumed (i.e. popped from the input stream)
        :param final: A boolean value specifying if the token is complete after the transition.
        :param mustSeeWhiteSpace: A boolean value specifying if the reduction only applies to white space lookahead symbols. Only takes effect if lookahead == '?'
        :param mustSeeKeyword: A boolean value specifying if the reduction only applies to lookahead symbols that constitute a keyword. Only takes effect if lookahead == '?'
        :param mustSeeIDSymbol: A boolean value specifying if the reduction only applies to lookahead symbols that represent identifier characters. Only takes effect if lookahead == '?'
        '''
        self._currentTokenState = currentTokenState
        self._lookahead = lookahead
        self._newTokenState = newTokenState
        self._append = append
        self._consume = consume
        self._final = final
        
        self._mustSeeWhiteSpace = mustSeeWhiteSpace
        self._mustSeeKeyWord = mustSeeKeyWord
        self._mustSeeIDSymbol = mustSeeIDSymbol
        
        
    def getCurrenTokenState(self):
        return self._currentTokenState
    
    def getLookahead(self):
        return self._lookahead
    
    def newTokenState(self):
        return self._newTokenState
    
    def getAppend(self):
        return self._append
    
    def getConsume(self):
        return self._consume
    
    def getFinal(self):
        return self._final
    
    def getMustSeeWhiteSpace(self):
        return self._mustSeeWhiteSpace
    
    def getMustSeeKeyWord(self):
        return self._mustSeeKeyWord
    
    def getMustSeeIDSymbol(self):
        return self._mustSeeIDSymbol
    
    
    