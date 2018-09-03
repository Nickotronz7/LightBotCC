import ply.yacc as yacc
import os
import codecs
import re
from main_Lex import tokens
from sys import stdin

precedence = ()

def p_programa(p):
	'''programa : variable BEGIN expresiones END procedimientos'''
	print ("program")
	#p[0] = program(p[1],"program")

def p_variable(p):
	'''variable : VAR ID variable1'''
	print ("variable")

def p_variable1(p):
	'''variable1 : ASSIGN NUM SEMICOLON'''
	print ("variable1")

def p_variable1_1(p):
	'''variable1 : SEMICOLON'''
	print ("variable1_1")
	
def p_expresiones1(p):
	'''expresiones : asignar expresiones'''
	print ("expresiones1")
		
def p_expresiones2(p):
	'''expresiones : actualizar expresiones'''
	print ("expresiones2")

def p_expresiones3(p):
	'''expresiones : cambiar_direccion expresiones'''
	print ("expresiones3")
		
def p_expresiones4(p):
	'''expresiones : colocar expresiones'''
	print ("expresiones4")
		
def p_expresiones5(p):
	'''expresiones : elevar expresiones'''
	print ("expresiones5")
		
def p_expresiones6(p):
	'''expresiones : encender expresiones'''
	print ("expresiones6")
		
def p_expresiones7(p):
	'''expresiones : mover expresiones'''
	print ("expresiones7")
		
def p_expresiones8(p):
	'''expresiones : pos_inicio expresiones'''
	print ("expresiones8")
		
def p_expresiones9(p):
	'''expresiones : llamar expresiones'''
	print ("expresiones9")
		
#def p_expresiones10(p):
#	'''expresiones : c_keep expresiones'''
#	print ("expresiones10")
		
#def p_expresiones11(p):
#	'''expresiones : c_for expresiones'''
#	print ("expresiones11")

#def p_expresiones12(p):
#	'''expresiones : c_when expresiones'''
#	print ("expresiones12")

def p_expresionesEpsilon(p):
	'''expresiones : epsilon'''
	print ("expresiones13")

def p_asignar(p):
	'''asignar : SET ID ASSIGN NUM SEMICOLON'''
	print ("asignar")
	
def p_actualizar(p):
	'''actualizar : ADD actualizar1'''
	print ("actualizar")
		
def p_actualizar_1(p):
	'''actualizar : LESS actualizar1'''
	print ("actualizar_1")
		
def p_actualizar1(p):
	'''actualizar1 : SUM ID SEMICOLON'''
	print ("actualizar1")
		
def p_cambiar_direccion(p):
	'''cambiar_direccion : CHANGEDIR LPAR direccion'''
	print ("cambiar_direccion")
			
def p_direccion_1(p):
	'''direccion : LEFT RPAR'''
	print ("direccion_1")
				
def p_direccion_2(p):
	'''direccion : RIGHT RPAR'''
	print ("direccion_2")
				
def p_direccion_3(p):
	'''direccion : BACK RPAR'''
	print ("direccion_3")
				
def p_direccion_4(p):
	'''direccion : SAME RPAR'''
	print ("direccion_4")

def p_colocar(p):
	'''colocar : PLACE BLOCK colocar1'''
	print ("colocar")
				
def p_colocar1_1(p):
	'''colocar1 : SEMICOLON'''
	print ("colocar1_1")
				
def p_colocar1_2(p):
	'''colocar1 : NUM SEMICOLON'''
	print ("colocar1_2")
	
def p_elevar(p):
	'''elevar : HIGH BLOCK elevar1'''
	print ("elevar")
				
def p_elevar1_1(p):
	'''elevar1 : SEMICOLON'''
	print ("elevar1_1")
				
def p_elevarr1_2(p):
	'''elevar1 : NUM SEMICOLON'''
	print ("elvar1_2")
				
def p_encender(p):
	'''encender : PUT LIGHT SEMICOLON'''
	print ("encender")
				
def p_mover(p):
	'''mover : POS LPAR NUM COMMA NUM RPAR SEMICOLON'''
	print ("mover")
					
def p_pos_inicio(p):
	'''pos_inicio : POSSTART LPAR NUM COMMA NUM RPAR SEMICOLON'''
	print ("pos_inicio")
					
def p_llamar(p):
	'''llamar : CALL ID SEMICOLON'''
	print ("llamar")
				
def p_procedimientos_1(p):
	'''procedimientos : PROC ID expresiones PREND'''
	print ("procedimientos_1")

def p_procedimientos_2(p):
	'''procedimientos : epsilon'''
	print ("procedimientos_2")

def p_epsilon(p):
	'''epsilon :'''
	print ("procedimientos")

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
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = str(input('\nNumero del test: '))
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]
'''

#directorio = "C:\\Users\\DEMEN\\Desktop\\LightBotCC\\LightBotCC-master\\src\\"
#archivo = buscarFicheros(directorio)
test = 'prueba1.LBcc.txt'
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc('LALR')
result = parser.parse(cadena)

print (result)
