'''
Created on 14.04.2015

@author: gereon
'''

class ContextStatement(object):
    '''
    Represents a mathematical statement that depends on a context.
    '''

    def __init__(self, context, statement):
        '''
        Creates a new context statement
        '''
        self._context
        self._statement
        
    def getContext(self):
        return self._context
    
    def getStatement(self):
        return self._statement
    
    def __str__(self):
        return "{context} ⊢ {statement}".format(context=self._context, statement=self._statement)