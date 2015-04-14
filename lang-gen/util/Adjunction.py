'''
Created on 14.04.2015

@author: gereon
'''

from Context import Context

class Adjunction(Context):
    '''
    Represents a context adjunction, which is itself a context.
    '''

    def __init__(self, context, updates):
        '''
        Creates a new context adjunction
        '''
        self._original = context
        self._updates = updates
        
    def getOriginal(self):
        return self._original
    
    def getUpdates(self):
        return self._updates
    
    def __str__(self):
        
        u = ""
        prefix = ""
        for (x, y) in sorted(self._updates.iteritems(), key=lambda (x, y) : x.getName()):
            u += prefix + "{x} := {y}".format(x=x, y=y)
            prefix = ", "
        
        return "{original}[{updates}]".format(original=self._original, updates=u)