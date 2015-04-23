'''
Created on 22.04.2015

@author: gereon
'''

class LexPosition(object):
    '''
    Represents the position a lexer is at
    '''

    def __init__(self, language, wordCount=0, row=0, column=0):
        '''
        Constructor
        '''
        self._lang = language
        self._wordCount = wordCount
        self._row = row
        self._column = column
        
    def advance(self, words):
        for w in words:
            self._wordCount += 1
            if w == self._lang.getNewLineCode():
                self._row += 1
                self._column = 0
            else:
                self._column += 1
        
    def getWordCount(self):
        return self._wordCount
    
    def getRow(self):
        return self._row
    
    def getColumn(self):
        return self._column