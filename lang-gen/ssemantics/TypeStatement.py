'''
Created on 14.04.2015

@author: gereon
'''

from util.Statement import Statement

class TypeStatement(Statement):
    '''
    Represents an assertion of a value having a certain type
    '''

    def __init__(self, value, _type):
        '''
        Creates a new type statement
        '''
        self._value = value
        self._type = _type
        
    def getValue(self):
        return self._value
    
    def getType(self):
        return self._type
    
    def __str__(self):
        return "{v} : {t}".format(v=self._value, t=self._type)