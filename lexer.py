#!/usr/bin/python
# This Python file uses the following encoding: utf-8
#from __future__ import annotations
import os, sys
import ply.lex as lex
import re

'''
Tokens type in Dart
Reservered words:
assert     break       case         catch
class      const       continue     default
do         else        enum         extends
false      final       finally      for
if         in          is           new
null       rethrow     return       super
switch     this        throw        true
try        var         void         while
with

Dart define:
LETTER:
    'a'..'z'|
    'A'..'Z'
;
DIGIT:
    '0'..'9'
;
WHITESPACE:
    ('\t'|''|NEWLINE)+
;

---Comments---
SINGLELINECOMMENT:
    '//'~(NEWLINE)* (NEWLINE)?
;
MULTILINECOMMENT:
    '/*'(MULTILINECOMMENT| ~*/')* */'
;

Description     Operator                           Associativity       Precedence
Unary postfix   ., ?., e++, e–, e1[e2], e1() , ()  None                16
Unary prefix    -e, !e,  ̃e, ++e, –e                None                15
Multiplicative  *, /, ̃/, %                         Left                14
Additive        +, -                               Left                13
Shift           <<,>>                              Left                12
Bitwise AND     &                                  Left                11
Bitwise XOR     ˆ                                  Left                10
Bitwise Or      |                                  Left                9
Relational      <,>,<=,>=,as,is,is!                None                8
Equality        ==, !=                             None                7
Logical AND     &&                                 Left                6
Logical Or      ||                                 Left                5
If-null         ??                                 Left                4
Conditional     e1?  e2:  e3                       Right               3
Cascade         ..                                 Left                2
Assignment      =, *=, /=, +=, -= ,&=, ˆ= etc.     Right               1

Constant Variables never uses lower case letter just uses underscored like:
PI, I_AM_A_CONSTANT

For function uses a lower case at the begin and no constant variables like:
camlCase dartForTheWin

Types of variables start with an upper case letter like:
DartType

Types can be short (one or more letters) like:
V S T B

For library never use upper case letters like:
my_favorite_library

'''

tokens = [
    #IDENTIFIERS
    'ID',
    #COMMENTS
    'SINGLE_COM',
    'MULTI_COM',
    #LITERALS
    'LIT_STRING', # "HOla"
    'LIT_REAL', # 50.0
    'LIT_INT',
    #SYMBOLS
    'S_LPAREN', # (
    'S_RPAREN', # )
    'S_SEMI_COL', # ;
    'S_LBRACKET', # [
    'S_RBRACKET', # ]
    'S_LCURLY_BRACE', # {
    'S_RCURLY_BRACE', # }
    #FURTHER INFO https://www.tutorialspoint.com/dart_programming/dart_programming_operators.htm
    #ASSING OPERATORS
    'OP_ASSIGN_SIMPLE', # =
    'OP_ASSIGN_MULT', # *=
    'OP_ASSIGN_DIV', # /=
    'OP_ASSIGN_ADD', # +=
    'OP_ASSIGN_SUBTRACT', #-=
    #LOGICAL OPERATOR
    'OP_LOGIC_AND', # &&
    'OP_LOGIC_OR', # ||
    'OP_LOGIC_NOT', # !
    #ARITHMETIC OPERATOR
    'OP_ARITH_ADD', # +
    'OP_ARITH_SUBTRACT', # -
    'OP_ARTIH_UNARY_MINUS', # -r
    'OP_ARITH_MULTIPLY', # *
    'OP_ARITH_DIVIDE', # /
    'OP_ARITH_INTEGER_DIVIDE', # ~/
    'OP_ARITH_MODULE', # %
    'OP_ARITH_INCREMENT', # ++
    'OP_ARITH_DECREMENT', # --
    #OPERATOR EQUALITY AND RELATIONAL
    'OP_EQUALITY_GREATER_THAN', # >
    'OP_EQUALITY_LESSER_THAN', # <
    'OP_EQUALITY_GREATER_OR_EQUAL_THAN', # >=
    'OP_EQUALITY_LESSER_OR_EQUAL_THAN', # <=
    'OP_EQUALITY_EQUAL', # ==
    'OP_EQUALITY_NOT_EQUAL', # !=
    'OP_DOT',
    'ERROR'
]

# RESERVED WORD LIST
reserved = {
    #Token validation for
    'main': 'MAIN',
    'int' : 'INT',
    'double' : 'DOUBLE',
    'String' : 'STRING',
    'bool' : 'BOOLEAN',
    #
    #
    'assert' : 'ASSERT',
    'break' : 'BREAK',
    'case' : 'CASE',
    'catch' : 'CATCH',
    'class' : 'CLASS',
    'const' : 'CONST',
    'continue' : 'CONTINUE',
    'default' : 'DEFAULT',
    'do' : 'DO',
    'else' : 'ELSE',
    'enum' : 'ENUM',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'final' : 'FINAL',
    'finally': 'FINALLY',
    'for' : 'FOR',
    'if' : 'IF',
    'import' : 'IMPORT',
    'in' : 'IN',
    'is' : 'IS',
    'new' : 'NEW',
    'null' : 'NULL',
    'rethrow' : 'RETHROW',
    'return' : 'RETURN',
    'super' : 'SUPER',
    'switch' : 'SWITCH',
    'this' : 'THIS',
    'throw' : 'THROW',
    'true' : 'TRUE',
    'try' : 'TRY',
    #'var' : 'VAR',
    'void' : 'VOID',
    'while' : 'WHILE',
    'with' : 'WITH'
}

tokens = tokens + list(reserved.values())

#Regular Expressions
#Comments
def t_SINGLE_COM(t):
    r'//.*\n'
    pass

def t_MULTI_COM(t):
    r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
    pass


#SYMBOLS
t_S_LPAREN = r'\(' # (
t_S_RPAREN = r'\)' # )
t_S_SEMI_COL = r'\;' # ;
t_S_LBRACKET = r'\[' # [
t_S_RBRACKET = r'\]' # ]
t_S_LCURLY_BRACE = r'\{' # {
t_S_RCURLY_BRACE = r'\}' # }

#Operator EQUALITY
t_OP_EQUALITY_GREATER_OR_EQUAL_THAN = r'\>\=' # >=
t_OP_EQUALITY_LESSER_OR_EQUAL_THAN = r'\<\=' # <=
t_OP_EQUALITY_EQUAL = r'\=\=' # ==
t_OP_EQUALITY_NOT_EQUAL = r'\!\=' # !=
t_OP_EQUALITY_GREATER_THAN = r'\>' # >
t_OP_EQUALITY_LESSER_THAN = r'\<' # <

#Assign OPERATOR
t_OP_ASSIGN_MULT = r'\*\=' # *=
t_OP_ASSIGN_DIV = r'/\=' # /=
t_OP_ASSIGN_ADD = r'\+\=' # +=
t_OP_ASSIGN_SUBTRACT = r'\-\=' #-=
t_OP_ASSIGN_SIMPLE = r'\=' # =

#Logical OPERATOR
t_OP_LOGIC_AND = r'\&\&' # &&
t_OP_LOGIC_OR = r'\|\|' # ||
t_OP_LOGIC_NOT = r'\!' # !
t_OP_DOT = r'\.'

#ARITHMETIC OPERATOR
t_OP_ARITH_INTEGER_DIVIDE = r'\~\/' # ~/
t_OP_ARITH_INCREMENT = r'\+\+' # ++
t_OP_ARITH_DECREMENT = r'\-\-' # --
t_OP_ARITH_ADD = r'\+' # +
t_OP_ARITH_SUBTRACT = r'\-' # -
#NIP que hacer aqui
#t_OP_ARTIH_UNARY_MINUS', # -r
t_OP_ARITH_MULTIPLY = r'\*' # *
t_OP_ARITH_DIVIDE = r'\/' # /
t_OP_ARITH_MODULE = r'\%' # %

#IGNORED CHARACTERS
t_ignore_space = r'\s'
t_ignore_newline = r'\n'
t_ignore_tab = r'\t'
t_ignore_vcmd = r'\v'

#Lit
t_LIT_INT = r'[+-]?([0-9]+)'
t_LIT_REAL = r'[+-]?([0-9]+)(\.[0-9]+)'
t_LIT_STRING = r'(?:\'(?:[^\']+|\'\')*\'|\"(?:[^\"]+|\"\")*\")' # (?:\'(?:[^\']+|\'\')*\'|\"(?:[^"]+|\"\")*\")

def t_ID(t):
    r'[a-zA-Z_$][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, "ID")
    return t

# ERROR HANDLING OF ILLEGAL CHARACTERS
def t_error(t):
    print("\nIllegal character: '%s' encountered" % t.value[0])
    t.type = "ERROR"
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

# BUILD THE LEXER
engine = lex.lex()

if __name__ == '__main__':
    lex.runmain()
