import ply.yacc as yacc
import os
import codecs
import re

from main_Lex import tokens
from sys import stdin

from globalVar import _MAT as _mat
from globalVar import _ACTUALPOS as _actualPos
from globalVar import _POSSTART as _posStart
from globalVar import _VARIABLES as _variables
from globalVar import _SWITCH as _switch

from globalVar import printMat

global procedimientos
procedimientos = ""


def p_programa(p):
	'''programa : variable BEGIN expresiones END procedimientos'''
	global procedimientos
	procedimientos = p[5]
	#print(procedimientos)
#	print ("program")

def p_variable(p):
	'''variable : VAR variable1'''
#	print ("variable")

def p_variable1(p):
	'''variable1 : ID ASSIGN NUM SEMICOLON'''
	global _variables
	_variables[p[1]] = int(p[3])
#	print ("variable1")

def p_variable1_1(p):
	'''variable1 : ID SEMICOLON'''
	global _variables
	_variables[p[1]] = -1
#	print ("variable1_1")
	
def p_expresiones1(p):
	'''expresiones : asignar expresiones'''
#	print ("expresiones1")
		
def p_expresiones2(p):
	'''expresiones : actualizar expresiones'''
#	print ("expresiones2")

def p_expresiones3(p):
	'''expresiones : cambiar_direccion expresiones'''
#	print ("expresiones3")
		
def p_expresiones4(p):
	'''expresiones : colocar expresiones'''
#	print ("expresiones4")
		
def p_expresiones5(p):
	'''expresiones : elevar expresiones'''
#	print ("expresiones5")
		
def p_expresiones6(p):
	'''expresiones : encender expresiones'''
#	print ("expresiones6")
		
def p_expresiones7(p):
	'''expresiones : mover expresiones'''
#	print ("expresiones7")
		
def p_expresiones8(p):
	'''expresiones : pos_inicio expresiones'''
#	print ("expresiones8")
		
def p_expresiones9(p):
	'''expresiones : llamar expresiones'''
#	print ("expresiones9")
		
def p_expresiones10(p):
	'''expresiones : c_keep expresiones'''
#	print ("expresiones10")
		
def p_expresiones11(p):
	'''expresiones : c_for expresiones'''
#	print ("expresiones11")

def p_expresiones12(p):
	'''expresiones : c_when expresiones '''
#	print ("expresiones12")

def p_expresiones13(p):
	'''expresiones : SKIP SEMICOLON expresiones'''
#	print ("expresiones13")
	
def p_expresiones14(p):
	'''expresiones  : COMMENT expresiones'''
#	print("comentario")

def p_expresionesEpsilon(p):
	'''expresiones : epsilon'''
#	print ("epsilon")

def p_cicloFor(p):
	'''c_for : FOR ID ASSIGN NUM TIMES expresiones FEND SEMICOLON'''
#	print("cicloFor")

def p_cicloWhen(p):
	'''c_when : WHEN ID ASSIGN NUM THEN expresiones WHEND SEMICOLON'''
#	print("cicloWhen")

def p_cicloKeep(p):
	'''c_keep : KEEP expresiones KEND SEMICOLON'''
#	print("cicloKeep")

def p_asignar(p):
	'''asignar : SET ID ASSIGN NUM SEMICOLON'''
	global _variables
	_variables[p[2]] = int(p[4])
#	print ("asignar")
	
def p_actualizar(p):
	'''actualizar : ADD SUM ID SEMICOLON'''
	global _variables
	_variables[p[2]] +=1
#	print ("actualizar")
		
def p_actualizar_1(p):
	'''actualizar : LESS SUM ID SEMICOLON'''
	global _variables
	_variables[p[2]] -=1
#	print ("actualizar_1")
		
def p_cambiar_direccion(p):
	'''cambiar_direccion : CHANGEDIR LPAR direccion'''
#	print ("cambiar_direccion")
			
def p_direccion_1(p):
	'''direccion : LEFT RPAR'''
	global _actualPos
	_actualPos[2] = (_actualPos - 1 )%4
#	print ("direccion_1")
				
def p_direccion_2(p):
	'''direccion : RIGHT RPAR'''
	global _actualPos
	_actualPos[2] = (_actualPos + 1 )%4
#	print ("direccion_2")
				
def p_direccion_3(p):
	'''direccion : BACK RPAR'''
	global _actualPos
	_actualPos[2] = (_actualPos + 2 )%4
#	print ("direccion_3")
				
def p_direccion_4(p):
	'''direccion : SAME RPAR'''
	pass
#	print ("direccion_4")

def p_colocar(p):
	'''colocar : PLACE BLOCK colocar1'''
#	print ("colocar")
				
def p_colocar1_1(p):
	'''colocar1 : SEMICOLON'''
	global _mat
	global _actualPos
	_mat[_actualPos[0]][_actualPos[1]][0] = 0 
#	print ("colocar1_1")
				
def p_colocar1_2(p):
	'''colocar1 : NUM SEMICOLON'''
	global _mat
	global _actualPos
	global _switch
	print(_actualPos[2])
	tmp_dict = _switch[_actualPos[2]]
	print(tmp_dict)
	for i in range(0,int(p[1])):
		if (_actualPos[0]+i*tmp_dict[0] in range(0,8) and _actualPos[1]+i*tmp_dict[1] in range(0,8)):
			_mat[_actualPos[0] + i*tmp_dict[0]][_actualPos[1]+i*tmp_dict[1]][0] = 0 
		else:
			print("No se pueden colocar más bloque en esta dirección")
			i = int(p[1])
#	print ("colocar1_2")
	
def p_elevar(p):
	'''elevar : HIGH BLOCK elevar1'''
#	print ("elevar")
				
def p_elevar1_1(p):
	'''elevar1 : SEMICOLON'''
	global _mat
	global _actualPos
	_mat[_actualPos[0]][_actualPos[1]][0] = 1
#	print ("elevar1_1")
				
def p_elevarr1_2(p):
	'''elevar1 : NUM SEMICOLON'''
	global _mat
	global _actualPos
	_mat[_actualPos[0]][_actualPos[1]][0] = int(p[1])
#	print ("elvar1_2")
				
def p_encender(p):
	'''encender : PUT LIGHT SEMICOLON'''
	global _mat
	global _actualPos
	_mat[_actualPos[0]][_actualPos[1]][1] = not(_mat[_actualPos[0]][_actualPos[1]][1])
#	print ("encender")
				
def p_mover(p):
	'''mover : POS LPAR NUM COMMA NUM RPAR SEMICOLON'''
	global _actualPos
	_actualPos  = [int(p[3]),int(p[5])]
#	print ("mover")
					
def p_pos_inicio(p):
	'''pos_inicio : POSSTART LPAR NUM COMMA NUM RPAR SEMICOLON'''
	global _posStart	
	_posStart = [int(p[3]), int(p[5])]
	#printMat()
#	print ("pos_inicio")
					
def p_llamar(p):
	'''llamar : CALL ID SEMICOLON'''
#	print ("llamar")
				
def p_procedimientos_1(p):
	'''procedimientos : PROC ID expresiones ENDPROC SEMICOLON'''
#	print ("procedimientos_1")

def p_procedimientos_2(p):
	'''procedimientos : epsilon'''
#	print ("procedimientos_2")

def p_epsilon(p):
	'''epsilon :'''
#	print ("epsilon")

def p_error(p):
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)

'''
def buscarFicheros(directorio):
	ficheros = []
	files = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
	#	print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = str(input('\nNumero del test: '))
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

#	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]
'''

#directorio = "C:\\Users\\DEMEN\\Desktop\\LightBotCC\\LightBotCC-master\\src\\"
#archivo = buscarFicheros(directorio)
#test = 'prueba2.LBcc.txt'
#fp = codecs.open(test,"r","utf-8")
#cadena = fp.read()
#fp.close()

def analisisSintantico(txt):
	parser = yacc.yacc()
	result = parser.parse(txt)

