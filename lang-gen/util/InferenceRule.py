'''
Created on 14.04.2015

@author: gereon
'''

from Statement import Statement

class InferenceRule(Statement):
    '''
    Represents a logical rule with several premises and exactly one conclusion.
    '''

    def __init__(self, name, premises, conclusion):
        '''
        Creates a new inference rule
        '''
        self._premises = premises
        self._conclusion = conclusion
        self._name = name
        
    def getName(self):
        return self._name
    
    def getPremises(self):
        return self._premises
    
    def getConclusion(self):
        return self._conclusion