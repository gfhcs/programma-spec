'''
Created on 13.04.2015

@author: gereon
'''

class Construct(object):
    '''
    Represents a part of a document describing a programming language.
    '''

    def __init__(self, target):
        self._constituents = []
        self._parent = None
        self._target = target
        
    def addConstituent(self, c, index=-1):
        
        if c._parent is not None:
            raise Exception("The construct {c} already has a parent and can thus not be added as a constituent of {s}!".format(c=c, s=self))
        
        c._parent = self
        
        if index >= 0:
            self._constituents.insert(index, c)
        else:
            self._constituents.append(c)
    
    def removeConstituent(self, c):
        self._constituents.remove(c)
        c._parent = None
        
    def __iter__(self):
        return iter(self._constituents)
        
    def getParent(self):
        return self._parent
        
    def getTarget(self):
        return self._target
    
    def dump(self, target):
        
        if self._target != target:
            return
        
        for c in self._constituents:
            c.dump(target)
        