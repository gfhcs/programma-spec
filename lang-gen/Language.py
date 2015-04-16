'''
Created on 13.04.2015

@author: gereon
'''

from construction.DirectoryConstruct import DirectoryConstruct
from construction.FileConstruct import FileConstruct
from construction.TextConstruct import TextConstruct
from construction.TextSnippet import TextSnippet


class Language(object):
    '''
    Represents a programming language.
    '''
    
    def __init__(self, grammar=None, categories=[]):
        self._grammar = grammar
        self._categories = categories
        
        self._rootConstruct = DirectoryConstruct("output")
        self._dir_spec = DirectoryConstruct("spec")
        
        self._rootConstruct.addConstituent(self._dir_spec)
        
        self._buildLexSpec()
        
    
    def _buildLexSpec(self):
                
        self._lexicalSpec = FileConstruct("lex_spec_latex", "lexical_grammar.tex")
        t = TextConstruct()
        self._lexicalSpec.addConstituent(t)
        
        self._dir_spec.addConstituent(self._lexicalSpec)
        
        lex_spec_intro ='''
\chapter{Lexical grammar} \label{chp:lex}
The EI consumes a program $p \in A^\ast$ from left to right by splitting it up into tokens, which is defined by the sets
\[\begin{array}{@{}ccl}
LS  & := & \lbrace ?, Cmt, Smb, Bit, Wrd \rbrace \\
N_T & := & \lbrace \langle comment \rangle , \langle bits \rangle ,  \langle symbols \rangle ,  \langle keyword \rangle,  \langle id \rangle  \rbrace \\
K   & := & \lbrace \input{keywords.txt} \rbrace \\
D   & := & \lbrace w \in K \mid \vert w\vert=1 \rbrace \\
D_I   & := & \lbrace \lit{'}, \lit{●}, \lit{○} \rbrace \\    
\end{array}\]
and the function
\[lex : LS \times  A^\ast \times A^\ast  \rightarrow  N_T \times A^\ast \times A^\ast ,\]
\[\begin{array}{@{}lrrccc}
'''
        
        t.addConstituent(TextSnippet("lex_spec_latex", lex_spec_intro))
        
        for lr in self._grammar.getLexicalReductions():
            t.addConstituent(TextSnippet("lex_spec_latex", lr.toLaTeX()))
        
        
        lex_spec_outro ='''
\end{array}\]

where $\vert d \vert = \vert c \vert = \vert c' \vert = 1 \;\wedge\; cs \in A^\ast \;\wedge\; d \notin D_I $ and

\[ n(t) := \begin{cases} \langle keyword \rangle & t \in K \\
                         \langle id \rangle      & t \notin K   \end{cases}\]

For $p \in A^\ast$ and $lex(?, \epsilon, p) = (l, t, r)$ we define:

\[\begin{array}{@{}lcl}
label(p) & := & l \\
token(p) & := & (l, t) \\
rest(p)  & := & r
\end{array}\]

The function $tokenize : A^\ast \rightarrow T^\ast$, that is defined by

\[
tokenize(p) := \begin{cases} \epsilon                         & \invisible \leadsto p \vee p =\epsilon                       \\
                             tokenize(rest(p))                & label(p) = \langle comment \rangle \\
                             token(p) \circ tokenize(rest(p)) & otherwise                          \end{cases}
\]

converts a stream of characters into a stream of tokens.

For $i \in \lbrace\any\rbrace^\ast, s\in\lbrace \any, \invisible \rbrace^\ast,b \in \lbrace \lit{○}, \lit{●}  \rbrace^\ast, k \in K$ we define:

\[\begin{array}{@{}lcl}

\langle id \rangle      &::=& (\langle id \rangle, i) \\

\langle symbols \rangle &::=& (\langle symbols \rangle, s) \\

\langle bits \rangle    &::=& (\langle bits \rangle, b) \\

k                       &::=& (\langle keyword \rangle, k) \\

\end{array}\]
'''
        
        t.addConstituent(TextSnippet("lex_spec_latex", lex_spec_outro))
        
    def getCategories(self):
        return iter(self._categories)
    
    def setCategories(self, categories):
        self._categories = categories
    
    def getConcreteGrammar(self):
        return self._grammar

    def setConcreteGrammar(self, g):
        self._grammar = g

    def getLexicalSpecification(self):
        return self._lexicalSpec
        
    def generateParser(self):
        