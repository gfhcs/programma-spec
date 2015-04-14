'''
Created on 13.04.2015

@author: gereon
'''

from construction import Construct.Construct

class TextConstruct(Construct):
    '''
    Represents a part of a document that consists of a directory.
    '''
    
    def getFile(self):
        return self.getParent().getFile()
    
    def dump(self, target):
        
        if self._target != target:
            return
        
        for c in self._constituents:
            c.dump(target)
        