from AnalizadorSintactico import analisisSintantico
import os
import codecs
import re

from globalVar import _MAT as _mat
from globalVar import printMat
from globalVar import _VARIABLES as _variables

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
    global _variables
    printMat()
    #print (_variables)

    return 1                                                                        # Análisis realizado correctamente

main("prueba2.LBcc.txt")