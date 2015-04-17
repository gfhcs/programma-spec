'''
Created on 13.04.2015

@author: gereon
'''

from Construct import Construct
from DirectoryConstruct import DirectoryConstruct

import os.path

class FileConstruct(Construct):
    '''
    Represents a part of a document that consists of a directory.
    '''

    def __init__(self, fileName, targets):
        super(FileConstruct, self).__init__(targets)
        self._fileName = fileName
        self._file = None
        
    def getFileName(self):
        return self._fileName
    
    def getFullPath(self):
        if isinstance(self.getParent(), DirectoryConstruct):
            return  os.path.join(self.getParent().getFullDirectory(), self._fileName)
        else:
            return self._fileName
    
    def getFile(self):
        return self._file
    
    def dump(self, target=None):
        
        if not(target is None or target in self._targets):
            return
        
        with open(self.getFullPath(), 'w') as self._file:   
            for c in self._constituents:
                c.dump(target)
        