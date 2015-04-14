'''
Created on 14.04.2015

@author: gereon
'''

class Category(object):
    '''
    Represents an abstract component of a programming language
    '''

    def __init__(self, name, mainProduction, componentCategories):
        self._name = name
        self._mainProduction = mainProduction
        self._componentCategories = componentCategories

    def getName(self):
        return self._name
    
    def getMainProduction(self):
        return self._mainProduction
    
    def getComponentCategories(self):
        return self._componentCategories