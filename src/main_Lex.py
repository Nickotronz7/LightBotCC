import ply.lex as lex
import re
import codecs
import os
import sys



# Palabras reservadas
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

t_ignore = '\t'
def t_NUM(t):
    r'[0-9]+'
    print(t.value)
    return t
    
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_SUM = r'\+'
t_RES = r'\-'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRA = r'\['
t_RBRA = r'\]'
t_COMMA = r'\,'
t_QUOTE = r'\"'
t_LCBRA = r'\{'
t_RCBRA = r'\}'


# Palabras Reservadas en expresiones regulares
t_PROC = r'Proc'
t_ENDPROC = r'End-Proc'
t_BEGIN = r'Begin'
t_END = r'End'
t_VAR = r'Var'
t_SET = r'Set'
t_ADD = r'Add'
t_LESS = r'Less'
t_LEFT = r'Left'
t_RIGHT = r'Right'
t_BACK = r'Back'
t_SAME = r'Same'
t_CHANGEDIR = r'ChangeDir'
t_PLACE = r'Place'
t_BLOCK = r'Block'
t_HIGH = r'High'
t_WHEN = r'When'
t_THEN = r'Then'
t_WHEND = r'Whend'
t_POSSTART = r'PosStart'
t_CALL = r'Call'
t_PUT = r'Put'
t_LIGHT = r'Light'
t_POS = r'Pos'
t_KEEP = r'Keep'
t_KEND = r'Kend'
t_SKIP = r'Skip'
t_FOR = r'For'
t_TIMES = r'Times'
t_FEND = r'Fend'
t_ID = r'[a-z]([a-zA-Z]|(\_|\@|\*)|[0-9]){0,9}'
t_MATHEXPR = r'(t_NUM(\+|-|\*|\\))*t_NUM'

def t_WHITESPACE(t):
    r'\s'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMMENT(t):
    r'\".*\"'
    pass

def t_error(t):
    print("Ilegal char '%s'" % t.value[0])
    t.lexer.skip(1)


#directorio = '~/Documents/LightBotCCLang/LightBotCC/tests/'
#archivo = open('/home/nickotronz7/Documents/LightBotCCLang/LightBotCC/tests/prueba1.nic')
#chain = archivo.read()
#archivo.close()

lexer = lex.lex()

#analizador.input(chain)

#while True:
#    tok = analizador.token()
#    if not tok: break
#    print (tok)