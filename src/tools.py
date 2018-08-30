case1 = "5+1"
case2 = "5+3-1"

z = ["+","-","/","*"]

exp = "5+1*3-9"

# funcion que retorna la cantidad de operadores de la exprecion
def getCantOps(string):
    index = 0
    cant = 0
    oPS = ["+","-","/","*"]
    while index < len(string):
        if string[index] in oPS:
            cant+=1
            index+=1
        else:
            index+=1
    return cant

# retorna un diccionario donde la key es le indice del operador y el value
# es el operador que esta en ese indice
def oPIndex(string):
    couter = 0
    cant = getCantOps(string)
    result = {}
    oPS = ["+","-","/","*"]
    if string == None:
        return result
    while couter < len(string) and cant > 0:
        if string[couter] in oPS:
            result.update({couter : string[couter]})
            couter+=1
            cant-=1
        else:
            couter+=1
    return result

# clasifica los operadores en 1 o 0 siendo 1 -> *,/ y 0 -> +,- basado en la
# prioridad de operaciones
def getOpType(op):
    type1 = ["/","*"]
    if op in type1:
        return 1
    else:
        return 0

# ordena el diccionario segun la prioridad de operadores
def sortOps(string, opsDic):
    type1 = {}
    type2 = {}
    key = 0
    while key < len(string):
        if opsDic.get(key) != None:
            if getOpType(opsDic.get(key)):
                type1.update({key : opsDic.get(key)})
                key+=1
            else:
                type2.update({key : opsDic.get(key)})
                key+=1
        else:
            key+=1

    type1.update(type2)
    return type1

def cArbol(string):
    #oPS = ["+","-","/","*"]
    if string == None:
        return []
    else:
        opIndex = oPIndex(string)
        #opType = getOpType(string[opIndex])
        return [string[opIndex-1], string[opIndex], string[opIndex+1]]


dic = oPIndex(case2)
print(sortOps(case2,dic))
