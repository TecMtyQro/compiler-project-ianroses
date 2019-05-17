from parser import *
from code_gen import *
from lex import *
import sys


def checkSemantic(text):
    terminals = []
    sysbolTable = []
    lex.input(text)
    while True:
        tok = lex.token()
        if not tok:
            break
        if tok.type == "ERROR":
            return "Error on Syntax (Lexer)"
        token = [tok.type, tok.value]
        terminals.append(token)
    dictionary = {}
    space = 0
    code = ""
    aux = ""
    last_var = None
    flag_assign = False
    while len(terminals) > 0:
        dictionary = {}
        #Checar los tipos de las
        if terminals[0][0] == 'IMPORT':
            terminals.pop(0)
            terminals.pop(0)
            terminals.pop(0)
        elif terminals[0][0] == 'VOID':
            if terminals[1][0] == 'MAIN':
                terminals.pop(0)
                terminals.pop(0)
                terminals.pop(0)
                terminals.pop(0)
                code += 'if __name__ =="__main__": \n'
        elif terminals[0][0] == 'IF':
            aux += ("  "*space)+ "if"
            terminals.pop(0)
            while terminals[0][1] != '{':
                aux += terminals[0][1]
                terminals.pop(0)
            terminals.pop(0)
            aux += ':'
            space += 2
            aux +="\n"
            code += aux
            aux = ""
        elif terminals[0][0] == 'ELSE' and terminals[1][0] == 'IF':
            aux += ("  "*space)+ "elif"
            terminals.pop(0)
            terminals.pop(0)
            while terminals[0][1] != '{':
                aux += terminals[0][1]
                terminals.pop(0)
            terminals.pop(0)
            aux += ':'
            space += 2
            aux +="\n"
            code += aux
            aux = ""
        elif terminals[0][0] == 'ELSE':
            aux += ("  "*space)+ "else"
            terminals.pop(0)
            while terminals[0][1] != '{':
                aux += terminals[0][1]
                terminals.pop(0)
            terminals.pop(0)
            aux += ':'
            space += 2
            aux +="\n"
            code += aux
            aux = ""
        elif terminals[0][0] == 'WHILE':
            aux += ("  "*space)+ "while"
            terminals.pop(0)
            while terminals[0][1] != '{':
                aux += terminals[0][1]
                terminals.pop(0)
            terminals.pop(0)
            aux += ':'
            space += 2
            aux +="\n"
            code += aux
            aux = ""
        elif terminals[0][0] == 'FOR':
            terminals.pop(0) #for
            aux += ("  "*space)+ "for "
            terminals.pop(0) #(
            terminals.pop(0) #int
            aux += terminals[0][1]+ " in range("
            terminals.pop(0) # month
            terminals.pop(0) # =
            aux += terminals[0][1]
            terminals.pop(0)
            terminals.pop(0)
            terminals.pop(0)
            if (terminals[0][1]== '<='):
                aux += ", 1+"
            else:
                aux += ","
            terminals.pop(0)
            aux+= terminals[0][1]
            terminals.pop(0)
            aux += '):'
            aux +="\n"
            code += aux
            aux = ""
            while (terminals[0][1] != "{"):
                terminals.pop(0)
        elif terminals[0][0] == 'S_LCURLY_BRACE':
            terminals.pop(0)
            space += 2
        elif terminals[0][0] == 'S_RCURLY_BRACE':
            terminals.pop(0)
            space -= 2
        elif terminals[0][0] == 'ID' and terminals[0][1] == 'print':
            aux += ("  "*space)+ "print"
            terminals.pop(0)
            while terminals[0][1] != ';':
                aux += terminals[0][1]
                terminals.pop(0)
            terminals.pop(0)
            aux += '\n'
            code += aux
            aux = ''
        #Variable declarations
        elif terminals[0][0] == 'STRING' or terminals[0][0] == 'INT' or terminals[0][0] ==  'DOUBLE':
            if twoInstance(sysbolTable,terminals[1][1], space):
                print("Error two declarations of the same variable")
                sys.exit()
            dictionary['type'] = terminals[0][0]
            terminals.pop(0)
            dictionary['name'] = terminals[0][1]
            aux += terminals[0][1]
            terminals.pop(0)
            dictionary['mutable'] = True
            dictionary['value'] = None
            dictionary['level'] = space
            #Variable assign
            if terminals[0][0] == 'OP_ASSIGN_DIV' or terminals[0][0] == 'OP_ASSIGN_ADD' or terminals[0][0] =='OP_ASSIGN_SUBTRACT' or terminals[0][0] =='OP_ASSIGN_MULT':
                print("ERROR ASSIGN: "+terminals[0][1])
                sys.exit()
            if terminals[0][0] == 'OP_ASSIGN_SIMPLE':
                aux += " = "
                terminals.pop(0)
                #input
                if terminals[0][0] == 'ID' and terminals[0][1] =='stdin':
                    while terminals[0][1] != ';':
                        terminals.pop(0)
                    # terminals.pop(0)
                    aux += "input()"
                    code+= ("  "*space)+aux
                    aux= ""
                    #sysbolTable.append(dictionary)
                elif terminals[0][0] == 'ID':
                    temp = getValueSys(sysbolTable, terminals[0][1], space)
                    if temp == None:
                        print ("Variable "+terminals[0][1]+" not define")
                        sys.exit()
                    if  isfloat(temp) and dictionary['type'] == 'DOUBLE':
                        dictionary['value'] = temp
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  isint(temp) and dictionary['type'] == 'INT':
                        dictionary['value'] = temp
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  temp and dictionary['type'] == 'STRING':
                        dictionary['value'] = temp
                        aux += terminals[0][1]
                        terminals.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                        sys.exit()
                elif  isfloat(terminals[0][1]) and dictionary['type'] == 'DOUBLE':
                    dictionary['value'] = terminals[0][1]
                    aux += terminals[0][1]
                    terminals.pop(0)
                elif  isint(terminals[0][1]) and dictionary['type'] == 'INT':
                    dictionary['value'] = terminals[0][1]
                    aux += terminals[0][1]
                    terminals.pop(0)
                elif  (terminals[0][1]) and dictionary['type'] == 'STRING':
                    dictionary['value'] = terminals[0][1]
                    aux += terminals[0][1]
                    terminals.pop(0)
                else:
                    print("ERROR No same type")
                    print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                    sys.exit()
                # if terminals[0][1] == ';':
                #     sysbolTable.append(dictionary)
                #     terminals.pop(0)
                #     code += ("  ")*space+aux+"\n"
                #     aux = ""
                # else:
                    # print("entro ahi")
                while terminals[0][1] != ';':
                    if terminals[0][1] == '+' or terminals[0][1] == '-' or terminals[0][1] == '*'or terminals[0][1] == '/' or terminals[0][1] == '%':
                        aux += " "+terminals[0][1]+" "
                        terminals.pop(0)
                    if terminals[0][0] == 'ID':
                        temp = getValueSys(sysbolTable, terminals[0][1], space)
                        if temp == None:
                            print ("Variable "+terminals[0][1]+" not define")
                            sys.exit()
                        if  isfloat(temp) and dictionary['type'] == 'DOUBLE':
                            dictionary['value'] = temp
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  isint(temp) and dictionary['type'] == 'INT':
                            dictionary['value'] = temp
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  temp and dictionary['type'] == 'STRING':
                            dictionary['value'] = temp
                            aux += terminals[0][1]
                            terminals.pop(0)
                        else:
                            print("ERROR No same type")
                            print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                            sys.exit()
                    elif  isfloat(terminals[0][1]) and dictionary['type'] == 'DOUBLE':
                        dictionary['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  isint(terminals[0][1]) and dictionary['type'] == 'INT':
                        dictionary['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  (terminals[0][1]) and dictionary['type'] == 'STRING':
                        dictionary['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                        sys.exit()
                if terminals[0][1] == ';':
                    sysbolTable.append(dictionary)
                    terminals.pop(0)
                    code += ("  ")*space+aux+"\n"
                    aux = ""
            else:
                sysbolTable.append(dictionary)
                terminals.pop(0)
                code += ("  ")*space+aux+" = None\n"
                aux = ""
        elif terminals[0][0] == 'CONST':
            terminals.pop(0)
            if terminals[0][0] == 'STRING' or terminals[0][0] == 'INT' or terminals[0][0] ==  'DOUBLE':
                if twoInstance(sysbolTable,terminals[1][1], space):
                    print("Error two declarations of the same variable")
                    sys.exit()
                dictionary['type'] = terminals[0][0]
                terminals.pop(0)
                dictionary['name'] = terminals[0][1]
                aux += terminals[0][1]
                terminals.pop(0)
                dictionary['mutable'] = False
                dictionary['value'] = None
                dictionary['level'] = space
                #Variable assign
                if terminals[0][0] == 'OP_ASSIGN_DIV' or terminals[0][0] == 'OP_ASSIGN_ADD' or terminals[0][0] =='OP_ASSIGN_SUBTRACT' or terminals[0][0] =='OP_ASSIGN_MULT':
                    print("ERROR ASSIGN: "+terminals[0][1])
                    sys.exit()
                if terminals[0][0] == 'OP_ASSIGN_SIMPLE':
                    aux += " = "
                    terminals.pop(0)
                    #input
                    if terminals[0][0] == 'ID' and terminals[0][1] =='stdin':
                        while terminals[0][1] != ';':
                            terminals.pop(0)
                        # terminals.pop(0)
                        aux += "input()"
                        code+= ("  "*space)+aux
                        aux= ""
                        #sysbolTable.append(dictionary)
                    elif terminals[0][0] == 'ID':
                        temp = getValueSys(sysbolTable, terminals[0][1], space)
                        if temp == None:
                            print ("Variable "+terminals[0][1]+" not define")
                            sys.exit()
                        if  isfloat(temp) and dictionary['type'] == 'DOUBLE':
                            dictionary['value'] = temp
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  isint(temp) and dictionary['type'] == 'INT':
                            dictionary['value'] = temp
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  temp and dictionary['type'] == 'STRING':
                            dictionary['value'] = temp
                            aux += terminals[0][1]
                            terminals.pop(0)
                        else:
                            print("ERROR No same type")
                            print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                            sys.exit()
                    elif  isfloat(terminals[0][1]) and dictionary['type'] == 'DOUBLE':
                        dictionary['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  isint(terminals[0][1]) and dictionary['type'] == 'INT':
                        dictionary['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  (terminals[0][1]) and dictionary['type'] == 'STRING':
                        dictionary['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                        sys.exit()
                    # if terminals[0][1] == ';':
                    #     sysbolTable.append(dictionary)
                    #     terminals.pop(0)
                    #     code += ("  ")*space+aux+"\n"
                    #     aux = ""
                    # else:
                        # print("entro ahi")
                    while terminals[0][1] != ';':
                        if terminals[0][1] == '+' or terminals[0][1] == '-' or terminals[0][1] == '*'or terminals[0][1] == '/' or terminals[0][1] == '%':
                            aux += " "+terminals[0][1]+" "
                            terminals.pop(0)
                        if terminals[0][0] == 'ID':
                            temp = getValueSys(sysbolTable, terminals[0][1], space)
                            if temp == None:
                                print ("Variable "+terminals[0][1]+" not define")
                                sys.exit()
                            if  isfloat(temp) and dictionary['type'] == 'DOUBLE':
                                dictionary['value'] = temp
                                aux += terminals[0][1]
                                terminals.pop(0)
                            elif  isint(temp) and dictionary['type'] == 'INT':
                                dictionary['value'] = temp
                                aux += terminals[0][1]
                                terminals.pop(0)
                            elif  temp and dictionary['type'] == 'STRING':
                                dictionary['value'] = temp
                                aux += terminals[0][1]
                                terminals.pop(0)
                            else:
                                print("ERROR No same type")
                                sys.exit()
                        elif  isfloat(terminals[0][1]) and dictionary['type'] == 'DOUBLE':
                            dictionary['value'] = terminals[0][1]
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  isint(terminals[0][1]) and dictionary['type'] == 'INT':
                            dictionary['value'] = terminals[0][1]
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  (terminals[0][1]) and dictionary['type'] == 'STRING':
                            dictionary['value'] = terminals[0][1]
                            aux += terminals[0][1]
                            terminals.pop(0)
                        else:
                            print("ERROR No same type")
                            print("Variable ",dictionary['name']," missmatch type ",terminals[0][1])
                            sys.exit()
                    if terminals[0][1] == ';':
                        sysbolTable.append(dictionary)
                        terminals.pop(0)
                        code += ("  ")*space+aux+"\n"
                        aux = ""
                else:
                    print("ERROR Const must get a value when assign")
                    sys.exit()
        elif terminals[0][0] == 'ID':
            temp = getElemSys(sysbolTable, terminals[0][1], space)
            aux = terminals[0][1]
            terminals.pop(0)
            if temp["mutable"] == False:
                print("ERROR Const can not change value")
                sys.exit()
####################################################################
            if (terminals[0][0] == 'OP_ASSIGN_DIV' or terminals[0][0] == 'OP_ASSIGN_ADD' or terminals[0][0] =='OP_ASSIGN_SUBTRACT' or terminals[0][0] =='OP_ASSIGN_MULT') and temp['value'] == None:
                print("ERROR ASSIGN: "+terminals[0][1])
                sys.exit()
            else:
                aux += " "+ terminals[0][1] +" "
                terminals.pop(0)
                #input
                if terminals[0][0] == 'ID' and terminals[0][1] =='stdin':
                    while terminals[0][1] != ';':
                        terminals.pop(0)
                    # terminals.pop(0)
                    aux += "input()"
                    code+= ("  "*space)+aux
                    aux= ""
                    #sysbolTable.append(dictionary)
                elif terminals[0][0] == 'ID':
                    temp2 = getValueSys(sysbolTable, terminals[0][1], space)
                    if temp2 == None:
                        print ("Variable "+terminals[0][1]+" not define")
                        sys.exit()
                    if  isfloat(temp2) and temp['type'] == 'DOUBLE':
                        temp['value'] = temp2
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  isint(temp2) and temp['type'] == 'INT':
                        temp['value'] = temp2
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  temp2 and temp['type'] == 'STRING':
                        temp['value'] = temp2
                        aux += terminals[0][1]
                        terminals.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",temp['name']," missmatch type ",terminals[0][1])
                        sys.exit()
                elif  isfloat(terminals[0][1]) and temp['type'] == 'DOUBLE':
                    temp['value'] = terminals[0][1]
                    aux += terminals[0][1]
                    terminals.pop(0)
                elif  isint(terminals[0][1]) and temp['type'] == 'INT':
                    temp['value'] = terminals[0][1]
                    aux += terminals[0][1]
                    terminals.pop(0)
                elif  (terminals[0][1]) and temp['type'] == 'STRING':
                    temp['value'] = terminals[0][1]
                    aux += terminals[0][1]
                    terminals.pop(0)
                else:
                    print("ERROR No same type")
                    print("Variable ",temp['name']," missmatch type ",terminals[0][1])
                    sys.exit()
                # if terminals[0][1] == ';':
                #     sysbolTable.append(dictionary)
                #     terminals.pop(0)
                #     code += ("  ")*space+aux+"\n"
                #     aux = ""
                # else:
                    # print("entro ahi")
                while terminals[0][1] != ';':
                    if terminals[0][1] == '+' or terminals[0][1] == '-' or terminals[0][1] == '*'or terminals[0][1] == '/' or terminals[0][1] == '%':
                        aux += " "+terminals[0][1]+" "
                        terminals.pop(0)
                    if terminals[0][0] == 'ID':
                        temp2 = getValueSys(sysbolTable, terminals[0][1], space)
                        if temp2 == None:
                            print ("Variable "+terminals[0][1]+" not define")
                            sys.exit()
                        if  isfloat(temp2) and temp['type'] == 'DOUBLE':
                            temp['value'] = temp2
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  isint(temp2) and temp['type'] == 'INT':
                            temp['value'] = temp2
                            aux += terminals[0][1]
                            terminals.pop(0)
                        elif  temp2 and temp['type'] == 'STRING':
                            temp['value'] = temp2
                            aux += terminals[0][1]
                            terminals.pop(0)
                        else:
                            print("ERROR No same type")
                            sys.exit()
                    elif  isfloat(terminals[0][1]) and temp['type'] == 'DOUBLE':
                        temp['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  isint(terminals[0][1]) and temp['type'] == 'INT':
                        temp['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    elif  (terminals[0][1]) and temp['type'] == 'STRING':
                        temp['value'] = terminals[0][1]
                        aux += terminals[0][1]
                        terminals.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",temp['name']," missmatch type ",terminals[0][1])
                        sys.exit()
                if terminals[0][1] == ';':
                    #sysbolTable.append(dictionary)
                    setElemSys(sysbolTable, temp)
                    terminals.pop(0)
                    code += ("  ")*space+aux+"\n"
                    aux = ""




    #     print(terminals)
    #     print(aux)
    #     print("-------------")
    #     print(code)
    #
    #     input()
    print(sysbolTable)
    return code







def twoDeclarations(symbolTable):
    for element in symbolTable:
        if element['name'] == '':
            return True
    return False

def twoInstance(sysbolTable, name, space):
    for element in sysbolTable:
        if element['name'] == name:
            if elemet['level']== space:
                return True
    return False

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def isint(value):
  try:
    float(value)
    return float(value).is_integer()
  except ValueError:
    return False

def getValueSys(sysbolTable, name, space):
    a = None
    cont = 0
    for elemet in sysbolTable:
        if elemet['name'] == name:
            if elemet['level'] == space:
                return elemet['value']
            if elemet['level'] < space and cont < space:
                cont = space
                a = elemet['value']
    return a

def getElemSys(sysbolTable, name, space):
    a = None
    cont = 0
    for elemet in sysbolTable:
        if elemet['name'] == name:
            if elemet['level'] == space:
                #print(elemet)
                return elemet
            if elemet['level'] < space and cont < space:
                cont = space
                a = elemet
    #print(a)
    return a

def setElemSys(sysbolTable, temp):
    for elemet in sysbolTable:
        if elemet['name'] == temp['name'] and elemet['level'] == temp['level']:
            elemet = temp
