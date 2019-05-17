import sys
import lex
from node import *
import ply.yacc as yacc

# Get the token map
tokens = lex.tokens

# terminals
x = []

# precedence = (
#     ('left', 'OP_LOGIC_AND', 'OP_LOGIC_OR'),
#     ('left', 'OP_ASSIGN_SIMPLE', 'OP_ASSIGN_MULT','OP_ASSIGN_DIV','OP_ASSIGN_ADD', 'OP_ASSIGN_SUBTRACT'),
#     ('nonassoc', 'OP_EQUALITY_EQUAL'),
#     ('left', 'OP_EQUALITY_GREATER_THAN', 'OP_EQUALITY_LESSER_THAN',
#      'OP_EQUALITY_GREATER_OR_EQUAL_THAN', 'OP_EQUALITY_LESSER_OR_EQUAL_THAN'),
#     ('left', 'OP_ARITH_ADD', 'OP_ARITH_SUBTRACT', 'OP_ARITH_MODULE'),
#     ('left', 'OP_ARITH_MULTIPLY', 'OP_ARITH_DIVIDE'),
#     ('right', 'OP_LOGIC_NOT')
# )

#Aqui empieza el arbol
def p_root(t):
    '''
    root : import_main
    '''
    t[0] = Node("root", None, None, [t[1]])


def p_import_main(t):
    '''
    import_main : import_list main
    '''
    t[0] = Node("import_main", None, None, [t[1], t[2]])

#Import
def p_import_list_1(t):
    'import_list : empty'
    t[0] = Node("import_list", None, None, [t[1]])

def p_import_list_2(t):
    'import_list : import_statement'
    t[0] = Node("import_list", None, None, [t[1]])

def p_import_list_3(t):
    'import_list : import_list import_statement'
    t[0] = Node("statement_list", None, None, [t[1], t[2]])

def p_import_statement(t):
    'import_statement : import_expression semicolon'
    T = Node(t[2], t[2])
    t[0] = Node("import_statement", None, None, [t[1], T])

def p_import_expression(t):
    'import_expression : IMPORT LIT_STRING'
    T = Node(t[2], t[2])
    t[0] = Node('import_expression', None, None, [T])
    x.append(t[1])
    x.append(t[2])

def p_main(t):
    '''
    main : VOID MAIN S_LPAREN S_RPAREN S_LCURLY_BRACE statement_list S_RCURLY_BRACE
    '''
    x.append(t[1])
    x.append(t[2])
    x.append(t[3])
    x.append(t[4])
    x.append(t[5])
    t[0] = Node("main", None, None, [t[6]])

    x.append(t[7])


# statement-list
def p_statement_list_1(t):
    'statement_list : empty'
    t[0] = Node("statement_list", None, None, [t[1]])

def p_statement_list_2(t):
    'statement_list : statement'
    t[0] = Node("statement_list", None, None, [t[1]])

def p_statement_list_3(t):
    'statement_list : statement_list statement'
    t[0] = Node("statement_list", None, None, [t[1], t[2]])

# statement
def p_statement(t):
    '''
    statement : expression_statement
              | selection_statement
              | iteration_statement
    '''
    t[0] = Node("statement", None, None, [t[1]])

# import-statement

# expression-statement
def p_expression_statement_1(t):
    'expression_statement : declaration_expression semicolon'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

def p_expression_statement_2(t):
    'expression_statement : empty semicolon'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

def p_expression_statement_3(t):
    'expression_statement : input_expression semicolon'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

def p_expression_statement_4(t):
    'expression_statement : output_expression semicolon'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

#import-expression
def p_import_expression(t):
    'import_expression : IMPORT LIT_STRING'
    T = Node(t[2], t[2])
    t[0] = Node('import_expression', None, None, [T])
    x.append(t[1])
    x.append(t[2])
# declaration-expression
def p_declaration_expression_1(t):
    'declaration_expression : assignment_expression'
    t[0] = Node("declaration_expression", None, None, [t[1]])

def p_declaration_expression_2(t):
    'declaration_expression : type_specifier declaration_expression'
    t[0] = Node("declaration_expression", None, None, [t[1], t[2]])

def p_declaration_expression_3(t):
    'declaration_expression : CONST type_specifier declaration_expression'
    T = Node(t[1], t[1])
    t[0] = Node("declaration_expression", None, None, [T, t[2], t[3]])
    x.append(t[1])

# selection-statement
def p_selection_statement_1(t):
    'selection_statement : IF conditional_expression block_statement_list'
    T = Node(t[1], t[1])
    t[0] = Node("selection_statement", None, None, [T, t[2], t[3]])
    x.append(t[1])

def p_selection_statement_2(t):
    'selection_statement : selection_statement ELSE IF conditional_expression block_statement_list'
    T1 = Node(t[2], t[2])
    T2 = Node(t[3], t[3])
    t[0] = Node("selection_statement", None, None, [t[1], T1, T2, t[4], t[5]])
    x.append(t[2])
    x.append(t[3])

def p_selection_statement_3(t):
    'selection_statement : selection_statement ELSE block_statement_list'
    T = Node(t[2], t[2])
    t[0] = Node("selection_statement", None, None, [t[1], T, t[3]])
    x.append(t[2])

# iteration-statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE conditional_expression block_statement_list'
    T = Node(t[1], t[1])
    t[0] = Node("iteration_statement", None, None, [T, t[2], t[3]])
    x.append(t[1])

def p_iteration_statement_2(t):
    'iteration_statement : DO block_statement_list WHILE conditional_expression'
    T1 = Node(t[1], t[1])
    T2 = Node(t[3], t[3])
    t[0] = Node("iteration_statement", None, None, [T1, t[2], T2, t[4]])
    x.append(t[1])
    x.append(t[3])

def p_iteration_statement_3(t):
    'iteration_statement : FOR S_LPAREN declaration_expression S_SEMI_COL logical_expression S_SEMI_COL ID OP_ARITH_INCREMENT S_RPAREN block_statement_list'
    T1 = Node(t[1], t[1])
    T2 = Node(t[2], t[2])
    T4 = Node(t[4], t[4])
    T6 = Node(t[6], t[6])
    T7 = Node(t[7], t[7])
    T8 = Node(t[8], t[8])
    T9 = Node(t[9], t[9])
    t[0] = Node("iteration_statement", None, None, [T1, T2, t[3], T4, t[5], T6, T7, T8, T9, t[10]])
    x.append(t[1])
    x.append(t[2])
    x.append(t[4])
    x.append(t[6])
    x.append(t[7])
    x.append(t[8])
    x.append(t[9])

def p_iteration_statement_4(t):
    'iteration_statement : FOR S_LPAREN declaration_expression  logical_expression ID OP_ARITH_DECREMENT S_RPAREN block_statement_list'
    T1 = Node(t[1], t[1])
    T2 = Node(t[2], t[2])
    T5 = Node(t[5], t[5])
    T6 = Node(t[6], t[6])
    T7 = Node(t[7], t[7])
    t[0] = Node("iteration_statement", None, None, [T1, T2, t[3], t[4], T5, T6, T7, t[8]])
    x.append(t[1])
    x.append(t[2])
    x.append(t[5])
    x.append(t[6])
    x.append(t[7])

# block-statement-list
def p_block_statement_list_1(t):
    'block_statement_list : S_LCURLY_BRACE statement_list S_RCURLY_BRACE'
    T1 = Node(t[1], t[1])
    T2 = Node(t[3], t[3])
    t[0] = Node("block_statement_list", None, None, [T1, t[2], T2])
    x.append(t[1])
    x.append(t[3])

# conditional-statement
def p_conditional_expression_1(t):
    'conditional_expression : S_LPAREN logical_expression S_RPAREN'
    T1 = Node(t[1], t[1])
    T2 = Node(t[3], t[3])
    t[0] = Node("conditional_expression", None, None, [T1, t[2], T2])
    x.append(t[1])
    x.append(t[3])

# assignment-expression
def p_assignment_expression_1(t):
    'assignment_expression : variable_expression'
    t[0] = Node("assignment_expression", None, None, [t[1]])

def p_assignment_expression_2(t):
    '''
    assignment_expression : assignment_expression OP_ASSIGN_SIMPLE logical_expression
                        | assignment_expression OP_ASSIGN_MULT logical_expression
                        | assignment_expression OP_ASSIGN_DIV logical_expression
                        | assignment_expression OP_ASSIGN_ADD logical_expression
                        | assignment_expression OP_ASSIGN_SUBTRACT logical_expression
    '''
    T = Node(t[2], t[2])
    t[0] = Node("assignment_expression", None, None, [t[1], T, t[3]])
    x.append(t[2])

def p_assignment_expression_3(t):
    '''
    assignment_expression : assignment_expression OP_ASSIGN_SIMPLE input_expression
                        | assignment_expression OP_ASSIGN_MULT input_expression
                        | assignment_expression OP_ASSIGN_DIV input_expression
                        | assignment_expression OP_ASSIGN_ADD input_expression
                        | assignment_expression OP_ASSIGN_SUBTRACT input_expression
    '''
    T = Node(t[2], t[2])
    t[0] = Node("assignment_expression", None, None, [t[1], T, t[3]])
    x.append(t[2])

# logical-expression:
def p_logical_expression_1(t):
    'logical_expression : equality_expression'
    t[0] = Node("logical_expression", None, None, [t[1]])

def p_logical_expression_2(t):
    'logical_expression : logical_expression logical_operators equality_expression'
    t[0] = Node("logical_expression", None, None, [t[1], t[2], t[3]])

# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    t[0] = Node("equality_expression", None, None, [t[1]])

def p_equality_expression_2(t):
    'equality_expression : equality_expression equality_operators relational_expression'
    t[0] = Node("equality_expression", None, None, [t[1], t[2], t[3]])

# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : math_expression'
    t[0] = Node("relational_expression", None, None, [t[1]])

def p_relational_expression_2(t):
    'relational_expression : relational_expression relational_operators math_expression'
    t[0] = Node("relational_expression", None, None, [t[1], t[2], t[3]])

# math-expression
def p_math_expression_1(t):
    'math_expression : primary_expression'
    t[0] = Node("math_expression", None, None, [t[1]])

def p_math_expression_2(t):
    'math_expression : math_expression math_operators primary_expression'
    t[0] = Node("math_expression", None, None, [t[1], t[2], t[3]])

# input-expression
def p_input_expression(t):
    'input_expression : ID OP_DOT ID S_LPAREN S_RPAREN'
    T1 = Node(t[1], t[1])
    T2 = Node(t[2], t[2])
    T3 = Node(t[3], t[3])
    T4 = Node(t[4], t[4])
    T5 = Node(t[5], t[5])
    t[0] = Node("input_expression", None, None, [T1, T2, T3, T4, T5])
    x.append(t[1])
    x.append(t[2])
    x.append(t[3])
    x.append(t[4])
    x.append(t[5])

# output-expression
def p_output_expression(t):
    'output_expression : ID conditional_expression'
    T1 = Node(t[1], t[1])
    t[0] = Node("output_expression", None, None, [T1, t[2]])
    x.append(t[1])

''' TERMINALS '''
# type-specifier
def p_type_specifier(t):
    '''
    type_specifier : INT
                   | BOOLEAN
                   | STRING
                   | DOUBLE
    '''
    T = Node(t[1], t[1])
    t[0] = Node('type_specifier', None, None, [T])
    x.append(t[1])

# logical-operators
def p_logical_operators(t):
    '''
    logical_operators : OP_LOGIC_AND
                      | OP_LOGIC_OR
    '''
    T = Node(t[1], t[1])
    t[0] = Node('logical_operators', None, None, [T])
    x.append(t[1])

# equality-operators
def p_equality_operators(t):
    '''
    equality_operators : OP_EQUALITY_EQUAL
                       | OP_EQUALITY_NOT_EQUAL
    '''
    T = Node(t[1], t[1])
    t[0] = Node('equality_operators', None, None, [T])
    x.append(t[1])

# relational-operators
def p_relational_operators(t):
    '''
    relational_operators : OP_EQUALITY_LESSER_THAN
                         | OP_EQUALITY_GREATER_THAN
                         | OP_EQUALITY_LESSER_OR_EQUAL_THAN
                         | OP_EQUALITY_GREATER_OR_EQUAL_THAN
    '''
    T = Node(t[1], t[1])
    t[0] = Node('relational_operators', None, None, [T])
    x.append(t[1])

# math-operators
def p_math_operators(t):
    '''
    math_operators : OP_ARITH_ADD
                   | OP_ARITH_SUBTRACT
                   | OP_ARITH_MULTIPLY
                   | OP_ARITH_DIVIDE
                   | OP_ARITH_INTEGER_DIVIDE
                   | OP_ARITH_MODULE
                   | OP_ARITH_INCREMENT
                   | OP_ARITH_DECREMENT
    '''
    T = Node(t[1], t[1])
    t[0] = Node('math_operators', None, None, [T])
    x.append(t[1])
# primary-expression
def p_primary_expression(t):
    '''
    primary_expression :  variable_expression
                       |  boolean_expression
                       |  LIT_INT
                       |  LIT_REAL
                       |  LIT_STRING
    '''
    if isinstance(t[1], Node) == True:
        t[0] = Node('primary_expression', None, None, [t[1]])
    else:
        T = Node(t[1], t[1])
        t[0] = Node('primary_expression', None, None, [T])
        x.append(t[1])

# variable-expression
def p_variable_expression(t):
    '''
    variable_expression : ID
                        | CONST
    '''
    T = Node(t[1], t[1])
    t[0] = Node('variable_expression', None, None, [T])
    x.append(t[1])

def p_boolean_expression(t):
    '''
    boolean_expression : TRUE
                       | FALSE
    '''
    T = Node(t[1], t[1])
    t[0] = Node('boolean_expression', None, None, [T])
    x.append(t[1])

def p_semicolon(t):
    '''
    semicolon : S_SEMI_COL
    '''
    T = Node(t[1], t[1])
    t[0] = Node('boolean_expression', None, None, [T])
    x.append(t[1])

def p_empty(t):
    'empty : '
    T = Node('', '')
    t[0] = Node('empty', None, None, [T])

def p_error(t):
    print("PARSE ERROR:", t.value)
    sys.exit();

def emptyTerminals(x):
    while len(x) > 0:
        x.pop()

yacc.yacc(debug=1)
