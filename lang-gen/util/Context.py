'''
Created on 14.04.2015

@author: gereon
'''

class Context(object):
    '''
    Represents a mathematical function, that maps a domain set (often variable names) to an image set (values, types, ...)
    '''

    def __init__(self, name):
        '''
        Creates a new context object.
        '''
        self._name = name
        
        
    def getName(self):
        return self._name
    
    def __str__(self):
        return self._name