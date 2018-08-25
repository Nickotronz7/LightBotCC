
import codecs
import os
import re
import sys

import ply.lex as lex

reservadas = ['Proc', 'PrEnd', 'Begin', 'End', 'Var', 'Set', 'Add', 'Less',
    'Left', 'Right', 'Back', 'Same', 'ChangeDir', 'Place', 'Block', 'High', 
    'Put','Light', 'Pos', 'Keep', 'Kend', 'Skip', 'For', 'Times', 'Fend',
    'When', 'Whend', 'PosStart', 'Call'
]

tokens = reservadas + ['NUM', 'ESPECIAL', 'CHAR', 'ID', 'COMMENT', 'EOL', 
    'ASSING', 'SUM', 'RES', 'LPAR', 'RPAR', 'LBRA', 'RBRA',
    'COMMA', 'SEMICOLON', 'QUOTE', 'LCBRA', 'RCBRA', 'WHITESPACE', 'RESERVED'
]


t_ignore = '\t'
t_NUM = r'[0-9]+'
t_SEMICOLON = r'\;'
t_ASSING = r'='
t_WHITESPACE = r'\s'
t_SUM = r'\r'
t_RES = r'\-'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRA = r'\['
t_RBRA = r'\]'
t_COMMA = r','
t_QUOTE = r'"'
t_LCBRA = r'{'
t_RCBRA = r'}'


def t_ID(t):
    r'[a-z]([a-zA-Z]|(\_|\@|\*)|t_NUM)*'
    
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return

def t_COMMENT(t):
    r'^\/\/.*'
    pass

def t_error(t):
    print("Ilegal char '%s'" % t.value[0])
    t.lexer.skip(1)



directorio = '~/Documents/LightBotCCLang/LightBotCC/tests/'
archivo = open('/home/nickotronz7/Documents/LightBotCCLang/LightBotCC/tests/prueba1.nic')
chain = archivo.read()
archivo.close()

analizador = lex.lex()

analizador.input(chain)

while True:
    tok = analizador.token()
    if not tok: break
    print (tok)


