'''
Created on 14.04.2015

@author: gereon
'''

from Expression import Expression

class Variable(Expression):
    '''
    Represents a mathematical variable
    '''

    def __init__(self, name):
        '''
        Creates a new variable
        '''
        self._name = name
        
    def getName(self):
        return self._name
    
    
    def __str__(self):
        return self._name