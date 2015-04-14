'''
Created on 14.04.2015

@author: gereon
'''

from util.ContextStatement import ContextStatement
from TypeContext import TypeContext
from TypeStatement import TypeStatement

class TypeContextStatement(ContextStatement):
    '''
    Represents a mathematical statement that depends on a context.
    '''

    def __init__(self, context, statement):
        '''
        Creates a new context statement
        '''
        
        if not isinstance(context, TypeContext):
            raise Exception("{context} cannot be part of a TypeContextStatement because it is not a type context!".format(context=context))
        if not isinstance(statement, TypeStatement):
            raise Exception("{statement} cannot be part of a TypeContextStatement because it is not a type statement!".format(statement=statement))
        
        super(self, TypeContextStatement).__init__(context, statement)