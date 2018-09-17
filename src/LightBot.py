from AnalizadorSintactico import *
import os
import codecs
import re

from globalVar import _MAT as _mat
from globalVar import printMat
from globalVar import _VARIABLES as _variables
from globalVar import _PROC as _proc
from globalVar import _EXPRESIONES as _expresiones

def execute(_expresiones):
    print()
    print(_expresiones)
    print()
    global _proc, _variables
    _lineno = 0
    while(_lineno  < len(_expresiones)):
        if(_expresiones[_lineno][0] == "PosStart"):
            p_pos_inicio([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] == "Place" and len(_expresiones[_lineno][0] == 4)):
            p_colocar1_2([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] == "Place"):
            p_colocar1([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] =="Pos"):
            p_mover([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] == "Put"):
            p_encender([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] == "Call"):
            _expresiones = _expresiones[:_lineno] + _proc[_expresiones[_lineno][1]] + _expresiones[1+_lineno:]
            _lineno -=1
        elif(_expresiones[_lineno][0] == "Set"):
            p_asignar([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] == "High" and len(_expresiones[_lineno]) == 4):
            p_elevar1_2([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] == "High"):
            p_elevar1([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] =="Add"):
            p_actualizar([0] + _expresiones[_lineno])
        elif(_expresiones[_lineno][0] =="Less"):
            p_actualizar_1([0] + _expresiones[_lineno])
            
        elif(_expresiones[_lineno][0] == "When"):

            print()
            print("#############################")
            print(_variables[_expresiones[_lineno][1]] == int(_expresiones[_lineno][3]))
            print("#############################")
            print()

            fin = 1
            if (_variables[_expresiones[_lineno][1]] == int(_expresiones[_lineno][3])):
                while(_expresiones[_lineno+fin][0] != "Whend"):
                    fin+=1
                print("___________________________")
                print(_expresiones[:_lineno + fin][_lineno+1:])
                print("___________________________")   
                execute(_expresiones[:_lineno + fin][_lineno+1:])
                _lineno +=fin +1 
                
            else:
                while(_expresiones[_lineno+fin][0] != "Whend"):
                    fin += 1
                print("___________________________")
                print(_expresiones[:_lineno + fin][_lineno+1:])
                print("___________________________")
                _lineno += fin + 1


        elif(_expresiones[_lineno][0] == "Keep"):
            fin = 1
            from globalVar import _keep
            _keep [0] +=1
            while(_expresiones[_lineno+fin][0] != "Kend"):
                fin +=1
            while(_keep[0]!= 0):
                execute(_expresiones[:_lineno +fin][_lineno+1:])
            _lineno += fin
        elif(_expresiones[_lineno][0] == "Skip"):
            from globalVar import _keep
            _keep [0] -=1
        elif(_expresiones[_lineno][0] =="For"):
            fin = 1
            while(_expresiones[_lineno + fin][0] != "Fend"):
                fin +=1
            for k in range(0, int(_expresiones[_lineno][3])):
                execute(_expresiones[:fin + _lineno][_lineno+1:])
            _lineno += fin
        elif(len(_expresiones[_lineno]) == 5 and _expresiones[_lineno][2] =="Left"):
            p_cambiar_direccion1([0] + _expresiones[_lineno])
        elif(len(_expresiones[_lineno]) == 5 and _expresiones[_lineno][2] == "Right"):
            p_cambiar_direccion2([0] + _expresiones[_lineno])
        elif(len(_expresiones[_lineno]) == 5 and _expresiones[_lineno][2] == "Back"):
            p_cambiar_direccion3([0] + _expresiones[_lineno])
        elif(len(_expresiones[_lineno]) == 5 and _expresiones[_lineno][2] == "Same"):
            p_cambiar_direccion4([0] + _expresiones[_lineno])
        _lineno +=1
        #print(_lineno)


def main(route):
    file = ""
    try:
        fp = codecs.open(route,"r","utf-8")
        file = fp.read()
        fp.close()
        
    except FileNotFoundError as error1:
        print ("I/O error({0}): {1}".format(error1.errno, error1.strerror))
        return 0                                                                    # Error en el análisis

    global _mat

    for i in range(0,8):
        _mat += [[]]
        for j in range(0,8):
            _mat[i] += [[8,False]]

    analisisSintantico(file)
    global _expresiones

    execute(_expresiones)
    printMat()
    return 1                                                                        # Análisis realizado correctamente

main('prueba4.LBcc.txt')