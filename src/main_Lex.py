import ply.lex as lex
import re
import codecs
import os
import sys

from globalVar import _MAT as _mat

#####################################################################################
#                           Palabras reservadas                                     #
# Lista con los nombres de los tokens pertenecientes a cada expresión regular. En   #
# ella se incluyen tanto expresiones reservadas del lenguaje como expresiones para  #
# valores numéricos o definiciones de operaciones aritméticas básicas.              #
#####################################################################################

reservadas = ['PROC', 'ENDPROC', 'BEGIN', 'END', 'VAR', 'SET', 'ADD', 'LESS',
    'LEFT', 'RIGHT', 'BACK', 'SAME', 'CHANGEDIR', 'PLACE', 'BLOCK', 'HIGH',
    'PUT', 'LIGHT', 'POS', 'KEEP', 'KEND', 'SKIP', 'FOR', 'TIMES', 'FEND',
    'WHEN', 'THEN', 'WHEND', 'POSSTART', 'CALL'
]

tokens = reservadas + ['NUM', 'ESPECIAL', 'ID', 'COMMENT', 'EOL', 
    'ASSIGN', 'SUM', 'RES', 'LPAR', 'RPAR', 'LBRA', 'RBRA',
    'COMMA', 'SEMICOLON', 'QUOTE', 'LCBRA', 'RCBRA', 'WHITESPACE',
    'MATHEXPR'
]

# especial
#####################################################################################
#                           Expresiones regulares                                   #
# Expresiones regulares que definen los tokens pertenecientes al lenguaje.          #
#####################################################################################
t_ignore = '\t'
def t_NUM(t):
    r'[0-9]+'
    return t
    
t_SEMICOLON = r';'                                      # Expresión regular que hace match con el valor: ";"
t_ASSIGN = r'='                                         # Expresión regular que hace match con el valor: "="
t_SUM = r'\+'                                           # Expresión regular que hace match con el valor: "+"
t_RES = r'\-'                                           # Expresión regular que hace match con el valor: "-"
t_LPAR = r'\('                                          # Expresión regular que hace match con el valor: "("
t_RPAR = r'\)'                                          # Expresión regular que hace match con el valor: ")"
t_LBRA = r'\['                                          # Expresión regular que hace match con el valor: "["
t_RBRA = r'\]'                                          # Expresión regular que hace match con el valor: "]"
t_COMMA = r'\,'                                         # Expresión regular que hace match con el valor: ","
t_QUOTE = r'\"'                                         # Expresión regular que hace match con el valor: "
t_LCBRA = r'\{'                                         # Expresión regular que hace match con el valor: "{"
t_RCBRA = r'\}'                                         # Expresión regular que hace match con el valor: "}"

#####################################################################################
#                   Palabras Reservadas en expresiones regulares                    #
# Pertenecen a las expresiones regulares, pero son solamente parabras reservadas    #
# del lenguaje, representan funciones implícitas dentro de LightBotCC.              #
#####################################################################################

t_PROC = r'Proc'                                        # Expresión regular que hace match con el valor literal: "Proc" 
t_ENDPROC = r'End-Proc'                                 # Expresión regular que hace match con el valor literal: "End-Proc"
t_BEGIN = r'Begin'                                      # Expresión regular que hace match con el valor literal: "Begin"
t_END = r'End'                                          # Expresión regular que hace match con el valor literal: "End"
t_VAR = r'Var'                                          # Expresión regular que hace match con el valor literal: "Var"
t_SET = r'Set'                                          # Expresión regular que hace match con el valor literal: "Set"
t_ADD = r'Add'                                          # Expresión regular que hace match con el valor literal: "Add"
t_LESS = r'Less'                                        # Expresión regular que hace match con el valor literal: "Less"
t_LEFT = r'Left'                                        # Expresión regular que hace match con el valor literal: "Left"
t_RIGHT = r'Right'                                      # Expresión regular que hace match con el valor literal: "Right"
t_BACK = r'Back'                                        # Expresión regular que hace match con el valor literal: "Back"
t_SAME = r'Same'                                        # Expresión regular que hace match con el valor literal: "Same"
t_CHANGEDIR = r'ChangeDir'                              # Expresión regular que hace match con el valor literal: "ChangeDir"
t_PLACE = r'Place'                                      # Expresión regular que hace match con el valor literal: "Place"
t_BLOCK = r'Block'                                      # Expresión regular que hace match con el valor literal: "Block"
t_HIGH = r'High'                                        # Expresión regular que hace match con el valor literal: "High"
t_WHEN = r'When'                                        # Expresión regular que hace match con el valor literal: "When"
t_THEN = r'Then'                                        # Expresión regular que hace match con el valor literal: "Then"
t_WHEND = r'Whend'                                      # Expresión regular que hace match con el valor literal: "Whend"
t_POSSTART = r'PosStart'                                # Expresión regular que hace match con el valor literal: "PosStart"
t_CALL = r'Call'                                        # Expresión regular que hace match con el valor literal: "Call"
t_PUT = r'Put'                                          # Expresión regular que hace match con el valor literal: "Put"
t_LIGHT = r'Light'                                      # Expresión regular que hace match con el valor literal: "Light"
t_POS = r'Pos'                                          # Expresión regular que hace match con el valor literal: "Pos"
t_KEEP = r'Keep'                                        # Expresión regular que hace match con el valor literal: "Keep"
t_KEND = r'Kend'                                        # Expresión regular que hace match con el valor literal: "Kend"
t_SKIP = r'Skip'                                        # Expresión regular que hace match con el valor literal: "Skip"
t_FOR = r'For'                                          # Expresión regular que hace match con el valor literal: "For"
t_TIMES = r'Times'                                      # Expresión regular que hace match con el valor literal: "Times"
t_FEND = r'Fend'                                        # Expresión regular que hace match con el valor literal: "Fend"
t_ID = r'[a-z]([a-zA-Z]|(\_|\@|\*)|[0-9]){0,9}'         # Expresión regular que hace match con cualquier identificador o nombre de proceso.
t_MATHEXPR = r'(t_NUM(\+|-|\*|\\))*t_NUM'               # Expresión regular que hace match con cualquier valor correspondiente a un número o expresión matemática.

#####################################################################################
#                             Expresiones ignoradas                                 #
# Estas expresiones se ignoran. No se toman en cuenta en la etapa de análisis       #
# sintáctico, no hayu ninguna acción relacionada con ellos y no pertenecen a la     #
# gramática.                                                                        #
#####################################################################################

def t_WHITESPACE(t):                                    # Expresión regular que hace match con cualquier espacio en blanco.
    r'\s'
    pass


def t_newline(t):                                       # Expresión regular que hace match con el caracter correspondiente a la nueva línea.
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMMENT(t):                                       # Expresión regular que hace match con las lineas que inician con /*, correspondientes a comentarios.
    r'\".*\"$'
    pass

def t_error(t):                                         # Expresión regular que hace match con cualquier caractér no presente en el lenguaje.
    print("Ilegal char '%s'" % t.value[0])
    t.lexer.skip(1)

#####################################################################################
#                               Análisis léxico                                     #
# Se realiza una llamada al analizador léxico, de manera que se puedan reconocer    #
# tokens dentro del archivo generado. De esta manera se puede realizar el análisis  #
# sintáctico sin problemas.                                                         #
#####################################################################################
lexer = lex.lex()