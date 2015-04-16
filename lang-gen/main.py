# coding=utf8

'''
Created on 14.04.2015

@author: gereon
'''

from csyntax.ConcreteGrammar import ConcreteGrammar
from csyntax.LexicalReduction import LexicalReduction
from Language import Language


programma_grammar = ConcreteGrammar()

#  (currentTokenState, lookahead), (newTokenState, empty, append, consume, final), (mustSeeWhiteSpace, mustSeeKeyWord, mustSeeIDSymbol)=(False, False, False)):

# Comments:
programma_grammar.addLexicalReduction(LexicalReduction((None, "#"), ("comment", False,  False, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("comment", "#"), (None, True, False, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("comment", "?"), ("comment", True, False, True, False)))

# Data literals:
programma_grammar.addLexicalReduction(LexicalReduction((None, "●"), ("bit", True,  True, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction((None, "○"), ("bit", True, True, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("bit", "●"), ("bit", False, True, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("bit", "○"), ("bit", False, True, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("bit", "?"), ("bit", False, False, False, True)))

# Skip white space:
programma_grammar.addLexicalReduction(LexicalReduction((None, "?"), ("?", True,  False, True, False), (True, False, False)))

# Keywords:
programma_grammar.addLexicalReduction(LexicalReduction((None, "?"), ("?", True,  True, True, True), (False, True, False)))

# Identifiers:
programma_grammar.addLexicalReduction(LexicalReduction((None, "?"), ("id", True,  True, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("id", "?"), ("id", False, True, True, False)))
programma_grammar.addLexicalReduction(LexicalReduction(("id", "?"), ("id", False, False, False, True)))


programma_grammar.parse(
'''

''')

programma_categories = []

programma = Language(programma_grammar, programma_categories)

# We'd like to get the following:
# Generate a lexical specification
# Generate a lexer
# Generate a parser
# Generate a full language specification
# Generate a full compiler
# Generate some valid programs

# Roadmap:
# 1. Debug the stuff that outputs lexer_grammar.tex
# 2. Start building the grammar and attach all the necessary stuff to it.
#    This is about language design, not necessarily the framework so much.
# ...

if __name__ == '__main__':
    
    programma.getLexicalSpec().dump()