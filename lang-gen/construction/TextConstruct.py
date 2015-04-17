'''
Created on 13.04.2015

@author: gereon
'''

from Construct import Construct

class TextConstruct(Construct):
    '''
    Represents a part of a document that consists of text.
    '''
    
    def getFile(self):
        return self.getParent().getFile()
    
    def dump(self, target=None):
        
        if target is not None and target not in self._targets:
            return
        
        for c in self._constituents:
            c.dump(target)
        