'''
Created on 13.04.2015

@author: gereon
'''

from Construct import Construct

class TextSnippet(Construct):
    '''
    Represents a piece of information that can be attached to a certain component of a programming Language
    specification. Depending on what kind of document is to be generated from the specification, the information
    is going to be put out.
    '''

    def __init__(self, content, targets=None):
        '''
        Creates a new snippet.
        :param target: A string identifying the kind of document that this snippet is going to be used in.
        :param content: The output string of the snippet.
        '''
        super(TextSnippet, self).__init__(targets)
        self._content = content
        
    def dump(self, target=None):
        
        if target is not None and target not in self._targets:
            return
        
        self.getParent().getFile().write(self._content)