'''
Created on 13.04.2015

@author: gereon
'''

class GrammarExpression(object):
    '''
    Represents a constituent of the right-hand-side of a production rule.
    '''
        
    @staticmethod
    def parse(self, source):
        return Choice.parse(source)
    
from Choice import Choice