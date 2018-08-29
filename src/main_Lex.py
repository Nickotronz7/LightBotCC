
import codecs
import os
import re
import sys

import ply.lex as lex

reservadas = ['PROC', 'PREND', 'BEGIN', 'END', 'VAR', 'SET', 'ADD', 'LESS',
    'LEFT', 'RIGHT', 'BACK', 'SAME', 'CHANGEDIR', 'PLACE', 'BLOCK', 'HIGH',
    'PUT', 'LIGHT', 'POS', 'KEEP', 'KEND', 'SKIP', 'FOR', 'TIMES', 'FEND',
    'WHEN', 'WHEND', 'POSSTART', 'CALL'
]

tokens = reservadas + ['NUM', 'ESPECIAL', 'CHAR', 'ID', 'COMMENT', 'EOL', 
    'ASSING', 'SUM', 'RES', 'LPAR', 'RPAR', 'LBRA', 'RBRA',
    'COMMA', 'SEMICOLON', 'QUOTE', 'LCBRA', 'RCBRA', 'WHITESPACE', 'RESERVED'
]


t_ignore = '\t'
t_NUM = r'[0-9]+'
t_SEMICOLON = r'\;'
t_ASSING = r'='
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
t_PROC = r'Proc'
t_PREND = r'Prend'
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
t_WHEND = r'Whend'
t_POSSTART = r'PosStart'
t_CALL = r'Call'
t_ID = r'[a-z]([a-zA-Z]|(\_|\@|\*)|t_NUM){0,9}'

def t_WHITESPACE(t):
    r'\s'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

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

