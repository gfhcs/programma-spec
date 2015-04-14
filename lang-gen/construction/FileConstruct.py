'''
Created on 13.04.2015

@author: gereon
'''

from construction import Construct.Construct
from construction import DirectoryConstruct.DirectoryConstruct

class FileConstruct(Construct):
    '''
    Represents a part of a document that consists of a directory.
    '''

    def __init__(self, target, fileName):
        self._fileName = fileName
        self._file = None
        
    def getFileName(self):
        return self._fileName
    
    def getFullPath(self):
        if isinstance(self.getParent(), DirectoryConstruct):
            return  self.getParent().getFullDirectory() + self._fileName
        else:
            return self._fileName
    
    def getFile(self):
        return self._file
    
    def dump(self, target):
        
        if self._target != target:
            return
        
        with open(self.getFullPath(), 'w') as self._file:   
            for c in self._constituents:
                c.dump(target)
        