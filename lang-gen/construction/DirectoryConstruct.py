'''
Created on 13.04.2015

@author: gereon
'''
import os

from Construct import Construct

class DirectoryConstruct(Construct):
    '''
    Represents a part of a document that consists of a directory.
    '''

    def __init__(self, directory):
        self._dir = directory
        
    def getDirectory(self):
        return self._dir
    
    def getFullDirectory(self):
        if isinstance(self.getParent(), DirectoryConstruct):
            return  self.getParent().getFullDirectory() + self._dir
        else:
            return self._dir
    
    def dump(self, target):
        
        
        d = self.getFullDirectory()
        
        if not os.path.exists(d):
            os.makedirs(d)
        
        
        for c in self._constituents:
            c.dump(target)
        