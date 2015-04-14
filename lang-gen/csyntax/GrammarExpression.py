'''
Created on 13.04.2015

@author: gereon
'''
import abc

class GrammarExpression(object):
    '''
    Represents a constituent of the right-hand-side of a production rule.
    '''
        
    @staticmethod
    def parse(self, source):
        return Choice.parse(source)
    
    @abc.abstracthmethod
    def getTerminals(self):
        pass
    
    @abc.abstracthmethod
    def getNonTerminals(self):
        pass
    
from Choice import Choice