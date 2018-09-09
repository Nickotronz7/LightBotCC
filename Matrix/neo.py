import numpy as np
import random


def createSequence():
    sequence = ""
    
    for i in range (64):
        sequence += str(random.randint(0,9))

    return sequence


        

def becomeArray():

    sequence = createSequence()
    newSequence = []

    for i in range(len(sequence)):
        newSequence += sequence[0]
        sequence = sequence[1:]

    newSequence = list(map(int, newSequence))
    
    return newSequence



def becomeMatrix():

    sequenceArray = becomeArray()
    matrix = np.asarray(sequenceArray).reshape(8,8)

    return matrix

    
        
        
