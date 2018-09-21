import ply.yacc as yacc
import os
import codecs
import re

from main_Lex import tokens
from sys import stdin
#####################################################################################
#                  	Imports de elementos globales compartidas                   	#
# Se importan variables y funciones compartidas por la etapa inicial y la etapa de 	#
# análisis sintáctico, en las variables se almacenan valores tales como la posición #
# inicial del bot, posición actual de edición del mapa, un método para imprimir la 	#
# matriz en el terminal y una declaración switch para realizar rotaciones en la 	#
# dirección en que se colocan los elementos.										#
# También se tiene un diccionario con los valores actuales de las variables, para 	#
# así simplificar el proceso de actualización de nuevas varialbes o el uso de ellas #
# en procedimientos.																#
#####################################################################################
from globalVar import _MAT as _mat
from globalVar import _ACTUALPOS as _actualPos
from globalVar import _POSSTART as _posStart
from globalVar import _VARIABLES as _variables
from globalVar import _SWITCH as _switch
from globalVar import printMat
from globalVar import _PROC as _proc
from globalVar import _PASADA as _pasada
from globalVar import _EXPRESIONES as _expresiones

global _inside_proc
_inside_proc = [False, ""]
#####################################################################################
#                  		Definición de una gramática libre.			                #
# Se define una gramática libre de contexto que define la estructura general del un #
# programa lightBotCC, se define cada una de las cadenas de tokens que forman		#
# expresiones pertenecientes al lenguaje, de esta manera se puede realizar un 		#
# análisis sintáctico sobre el archivo input.										#
#####################################################################################

## Define la estructura principal de un programa, mediante la definición de 3 secciones
# principales, estas son la definición de variables, expresiones y la sección de 
# procedimientos.
def p_programa(p):
	'''programa : variable begin expresiones end procedimientos'''
	global _pasada
	_pasada = False

def p_begin(p):
	'''begin : BEGIN'''

def p_end(p):
	'''end : END'''

def p_variable(p):
	'''variable : variable1 var1'''
															# Estructura principal de una definición de variable
def p_var1(p):
	'''var1 : variable1 variable'''
def p_var1_2(p):
	'''var1 : epsilon'''

def p_variable1(p):
	'''variable1 : VAR ID ASSIGN NUM SEMICOLON'''				# Primera forma de definir una variable, se define de la forma:
#															# Var foo = NUM;
	
	global _variables
	_variables[p[2]] = int(p[4])						# Añade al diccionario de variables el nombre de la variable y 
#															# luego coloca el valor numérico de la variable en el diccionario
#															# en el índice correspondiente.

def p_variable1_1(p):
	'''variable1 : VAR ID SEMICOLON'''							# Segunda forma de definir una variable, se define de la forma:
#															# Var foo;
	global _variables
	_variables[p[1]] = -1									# Añade al diccionario de variables el nombre de la variable y 
#															# luego coloca elvalor por de la variable en el diccionario
#															# en el índice correspondiente, el valor correspondiente de una 
#															# variable no inicializada es -1.

## La sección de expresiones, se puede utilizar en múltiples sitios, se define su estructura
# primero como no terminales y más adelante se presenta su deficinión añadiendo tokens. 
def p_expresiones1(p):
	'''expresiones : asignar expresiones'''					# Expresión no terminal para asignar una variable
		
def p_expresiones2(p):
	'''expresiones : actualizar expresiones'''				# Expresión no terminal para cambiar el valor de una variable

def p_expresiones3(p):
	'''expresiones : cambiar_direccion expresiones'''		# Expresión no terminal para cambiar la dirección en la que se 
#															# van a colocar los próximos bloques.
		
def p_expresiones4(p):
	'''expresiones : colocar expresiones'''					# Expresión no terminal para colocar un bloque en la posición
#															# actual o múltiples bloques en una dirección específica. 
		
def p_expresiones5(p):
	'''expresiones : elevar expresiones'''					# Expresión no terminal para cambiar el nivel de un bloque.
		
def p_expresiones6(p):
	'''expresiones : encender expresiones'''				# Expresión no terminal para colocar una luz en la posición 
#															# actual. 
		
def p_expresiones7(p):
	'''expresiones : mover expresiones'''					# Expresión no terminal para cambiar la posición actual. 
		
def p_expresiones8(p):
	'''expresiones : pos_inicio expresiones'''				# Expresión no terminal para cambiar la posición inicial del 
#															# bot. 
		
def p_expresiones9(p):
	'''expresiones : llamar expresiones'''					# Expresión no terminal para llamar a un procedimiento.
		
def p_expresiones10(p):
	'''expresiones : c_keep expresiones'''					# Expresión no terminal que ejecuta el ciclo Keep.
		
def p_expresiones11(p):
	'''expresiones : c_for expresiones'''					# Expresión no terminal que ejecuta el ciclo For.

def p_expresiones12(p):
	'''expresiones : c_when expresiones '''					# Expresión no terminal querealiza la verificación When.

def p_expresiones13(p):
	'''expresiones : skip expresiones'''				# Expresión que termina el ciclo Keep.

def p_skip(p):
	'''skip : SKIP SEMICOLON'''
	if (addTo(p)):
		pass
	
def p_expresiones14(p):
	'''expresiones  : COMMENT expresiones'''				# Expresión que incluye los comentarios dentro de la gramática.

def p_expresiones15(p):
	'''expresiones : endproc procedimientos'''

def p_endproc(p):
	'''endproc : ENDPROC SEMICOLON'''
	
	global _inside_proc
	if (_inside_proc[0]):
		_inside_proc[0] = False
	else:
		print("Error, no se ha declarado un procedimiento correspondiente " + _inside_proc[1])

def p_expresiones16(p):
	'''expresiones : whend expresiones '''

def p_expresionesEpsilon(p):
	'''expresiones : epsilon'''								# Definición de la producción hilera vacía.

def p_cicloFor(p):
	'''c_for : FOR ID ASSIGN NUM TIMES '''	
#															# Definición explícita de un ciclo For, se  define:
#															# For foo = NUM Times expresiones Fend;
#															# Donde expresiones representa un no-terminal.
	addTo(p)


def p_expresiones18(p):
	'''expresiones : fend expresiones'''

def p_endCicloFor(p):
	'''fend : FEND SEMICOLON '''
	addTo(p)

def p_cicloWhen(p):
	'''c_when : WHEN ID ASSIGN NUM THEN '''
#															# Definicion explicita de una comparacion del tipo When, se define:
#															# When foo = NUM Then expresiones Whend;
	addTo(p)

def p_endCicloWhen(p):
	'''whend : WHEND SEMICOLON'''
	addTo(p)
		
def p_cicloKeep(p):
	'''c_keep : KEEP'''										# Definicion explicita del ciclo Keep, se define de la forma:
#															# Keep expresiones Kend;
#															# Donde el ciclo se detiene solamente si encuentra el valor Skip dentro
#															# de las expresiones.
	addTo(p)

def p_expresiones17(p):
	'''expresiones : kend expresiones'''

def p_endCicloKeep(p):
	'''kend : KEND SEMICOLON'''
	if (addTo(p)):
		pass
		
def p_asignar(p):
	'''asignar : SET ID ASSIGN NUM SEMICOLON'''				# Definición explícita para asignar valor a una variable, se utiliza:
#															# Set foo = NUM;
	if (addTo(p)):
		global _variables
		try:
			_variables[p[2]] = int(p[4])
		except:
			print("Variable " + p[2] + " no se encuentra definida con anterioridad.")
		
def p_actualizar(p):
	'''actualizar : ADD SUM ID SEMICOLON'''					# Definició explícita para aumentar en 1 una variable, se utiliza:
#															# Add+foo;
	if (addTo(p)):
		global _variables
		_variables[p[3]] +=1
		
def p_actualizar_1(p):
	'''actualizar : LESS SUM ID SEMICOLON'''				# Definición explícita para disminuir en 1 una variable, se utiliza:
#															# Less+foo;
	if (addTo(p)):
		global _variables
		_variables[p[3]] -=1
		
def p_cambiar_direccion1(p):
	'''cambiar_direccion : CHANGEDIR LPAR LEFT RPAR SEMICOLON'''								
#															# Actualiza el valor de la dirección en  que se colocan los bloques,
#															# rota hacia la izquierda relativa al frente actual. Se implementa:
#															# ChangeDir(LEFT);
	if (addTo(p)):
		global _actualPos
		_actualPos[2] = (_actualPos[2] - 1 )%4
			
				
def p_cambiar_direccion2(p):
	'''cambiar_direccion : CHANGEDIR LPAR RIGHT RPAR SEMICOLON'''
#															# Actualiza el valor de la dirección en que se colocan los bloques,
#															# rota hacia la derecha relativa al frente actual. Se implementa:
#															# ChangeDir(RIGHT);
	if (addTo(p)):
		global _actualPos
		_actualPos[2] = (_actualPos[2] + 1 )%4
				
def p_cambiar_direccion3(p):
	'''cambiar_direccion : CHANGEDIR LPAR BACK RPAR SEMICOLON'''
#															# Actualiza el valor de la dirección en que se colocan los bloques,
#															# invierte la dirección relativa al frente actual. Se implementa:
#															# ChangeDir(BACK);
	if (addTo(p)):
		global _actualPos
		_actualPos[2] = (_actualPos[2] + 2 )%4
				
def p_cambiar_direccion4(p):
	'''cambiar_direccion : CHANGEDIR LPAR SAME RPAR SEMICOLON'''
#															# Actualiza el valor de la dirección en que se colocan los bloques,
#															# se mantiene en la misma dirección que en la que se encontraba anteriormente.
#															# Se implementa:
#															# ChangeDir(SAME);
	if (addTo(p)):
		global _actualPos, _switch
		#print(_switch[_actualPos[2]][0])
		x = _actualPos[0] + _switch[_actualPos[2]][0]
		y = _actualPos[1] + _switch[_actualPos[2]][1]
		if (x in range(0,8)):
			_actualPos[0] = x
		if (y in range(0,8)):
			_actualPos[1] = y 

def p_colocar1(p):
	'''colocar : PLACE BLOCK SEMICOLON'''					# Definición de la intrucción para colocar 1 bloque en la posición actual
#															# Se implementa:
#															# Place Block;
	if (addTo(p)):
		global _mat
		global _actualPos
		_mat[_actualPos[0]][_actualPos[1]][0] = 0 
				
def p_colocar1_2(p):
	'''colocar : PLACE BLOCK NUM SEMICOLON''' 				# Definición de la intrucción para colocar n bloques en la direccion actual 
#															# Se implementa:
#															# Place Block;
	if (addTo(p)):
		global _mat
		global _actualPos
		global _switch

		#print(_actualPos[2])
		tmp_dict = _switch[_actualPos[2]]
		#print(tmp_dict)
		for i in range(0, int(p[3]) ):
			if (_actualPos[0]+i*tmp_dict[0] in range(0,8) and _actualPos[1]+i*tmp_dict[1] in range(0,8)):
				_mat[_actualPos[0] + i*tmp_dict[0]][_actualPos[1]+i*tmp_dict[1]][0] = 0 
			else:
				print("No se pueden colocar más bloque en esta dirección")
				i = int(p[3])
	
def p_elevar1(p):
	'''elevar : HIGH BLOCK SEMICOLON'''						# Definición de la intruccion para elevar en 1 nivel un bloque, se implementa:
#															# High Block;

	if (addTo(p)):
		global _mat
		global _actualPos
		_mat[_actualPos[0]][_actualPos[1]][0] = 1
				
def p_elevar1_2(p):
	'''elevar : HIGH BLOCK NUM SEMICOLON'''					# Definición de la intruccion para elevar en n el nivel un bloque, se implementa:
#															# High Block NUM
	if (addTo(p)):
		global _mat
		global _actualPos
		#print(p)
		_mat[_actualPos[0]][_actualPos[1]][0] = int(p[3])
				
def p_encender(p):
	'''encender : PUT LIGHT SEMICOLON'''
	if (addTo(p)):
		global _mat
		global _actualPos
		_mat[_actualPos[0]][_actualPos[1]][1] = not(_mat[_actualPos[0]][_actualPos[1]][1])
				
def p_mover(p):
	'''mover : POS LPAR ID COMMA ID RPAR SEMICOLON'''
	if (addTo(p)):
		global _actualPos, _variables
		if (p[3] in _variables):
			if (_variables[p[3]] in range (0,8)):
				_actualPos[0] = int(_variables[p[3]])
			else:
				print("Variable " + p[3] +" tiene un valor fuera de los límites = " +_variables[p[3]])
				return False
		else:
			print(p[3]+ " no es una variable declarada dentro del programa.")
			return False
		if (p[5] in _variables):
			if (_variables[p[5]] in range (0,8)):
				_actualPos[1] = int(_variables[p[5]])
			else:
				print("Variable " + p[5] +" tiene un valor fuera de los límites = " +_variables[p[5]])
				return False
		else:
			print(p[5] + " no es una variable declarada dentro del programa.")
			return False
		return True
					
def p_pos_inicio(p):
	'''pos_inicio : POSSTART LPAR ID COMMA ID RPAR SEMICOLON'''
	if (addTo(p)):
		global _posStart, _variables
		if (p[3] in _variables):
			if (_variables[p[3]] in range (0,8)):
				_posStart[0] = int(_variables[p[3]])
			else:
				print("Variable " + p[3] +" tiene un valor fuera de los límites = " +_variables[p[3]])
				return False
		else:
			print(p[3]+ " no es una variable declarada dentro del programa.")
			return False
		if (p[5] in _variables):
			if (_variables[p[5]] in range (0,8)):
				_posStart[1] = int(_variables[p[5]])
			else:
				print("Variable " + p[5] +" tiene un valor fuera de los límites = " +_variables[p[5]])
				return False
		else:
			print(p[5] + " no es una variable declarada dentro del programa.")
			return False
		return True
def p_llamar(p):
	'''llamar : CALL ID'''
	if (addTo(p)):
		pass
				
def p_procedimientos(p):
	'''procedimientos : procs expresiones'''

def p_procedimientos_1(p):
	'''procs : PROC ID'''
	global _proc
	if (p[2] in _proc):
		print("procedimiento ya definido")
		return
	else:
		_proc[p[2]] = []
		global _inside_proc
		_inside_proc[0] = True
		_inside_proc[1] = p[2]

def p_procedimientos_2(p):
	'''procs : epsilon'''

def p_epsilon(p):
	'''epsilon :'''

def p_error(p):
	print ("Error de sintaxis ", p)

def analisisSintantico(txt):
	parser = yacc.yacc()
	parser.parse(txt)
	
def addTo(p):
	global _pasada
	if (_pasada):
		global _inside_proc
		if (_inside_proc[0]):
			global _proc
			_proc[_inside_proc[1]]+=[p[1:]]
		else:
			global _expresiones
			_expresiones+=[p[1:]]
		return False
	else:
		return True