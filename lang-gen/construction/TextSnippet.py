'''
Created on 13.04.2015

@author: gereon
'''

class TextSnippet(object):
    '''
    Represents a piece of information that can be attached to a certain component of a programming Language
    specification. Depending on what kind of document is to be generated from the specification, the information
    is going to be put out.
    '''

    def __init__(self, target, content):
        '''
        Creates a new snippet.
        :param target: A string identifying the kind of document that this snippet is going to be used in.
        :param content: The output string of the snippet.
        '''
        
        self._target = target
        self._content = content
        
    def dump(self, target):
        
        if target != self._target:
            return
        
        self.getParent().getFile().write(self._content)