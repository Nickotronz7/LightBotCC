from AnalizadorSintactico import analisisSintantico
import os
import codecs
import re

global _mat
_mat = []

def main(route):
    file = ""
    try:
        fp = codecs.open(route,"r","utf-8")
        file = fp.read()
        fp.close()
        
    except FileNotFoundError as error1:
        print ("I/O error({0}): {1}".format(error1.errno, error1.strerror))
        return 0


    analisisSintantico(file)

    global _mat
    for i in range(0,8):
        _mat += [[]]
        for j in range(0,8):
            _mat[i] += [0]
        
        print(_mat[i])
    

main("prueba2.LBcc.txt")