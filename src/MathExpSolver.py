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
    result = []
    oPS = ['+','-','/','*']
    if string == None:
        return result
    while couter < len(string) and cant > 0:
        if string[couter] in oPS:
            result += [couter]
            couter+=1
            cant-=1
        else:
            couter+=1
    return result

# clasifica los operadores en 1 o 0 siendo 1 -> *,/ y 0 -> +,- basado en la
# prioridad de operaciones
def getOpType(op):
    type1 = ['/','*']
    if op in type1:
        return 1
    else:
        return 0

# ordena el diccionario segun la prioridad de operadores
def sortOps(string, opsList):
    type1 = []
    type2 = []
    for i in opsList:
        if getOpType(string[i]):
            type1 += [i]
        else:
            type2 += [i]
    type1 += type2
    return type1

#De String a lista con numeros
def stringToListWithNums(opIndex, string):
    cont = 0
    newList = []
    while cont < len(opIndex):
        if not cont:
            newList += [int(string[:opIndex[cont]]), string[opIndex[cont]]]
            cont +=1
        elif cont == (len(opIndex)-1):
            newList += [int(string[opIndex[cont-1]+1:opIndex[cont]]), string[opIndex[cont]], int(string[opIndex[cont]+1:])]
            return newList
        else:
            newList += [int(string[opIndex[cont-1]+1:opIndex[cont]]), string[opIndex[cont]]]
            cont +=1


# Funcion que crea el arbol compreto
def crearArbol(tree, opIndexList):
    if len(opIndexList) == 1:
        return tree
    else:
        n = opIndexList[0]
        tmp1 = tree[:n-1]
        tmp2 = [tree[n-1:n+2]]
        tmp3 = tree[n+2:]
        return crearArbol(tmp1+tmp2+tmp3, sortOps(tmp1+tmp2+tmp3,oPIndex(tmp1+tmp2+tmp3)))


# Funcion que setea el string para poder empezar a construir el arbol
def getTree(string):
    opIndex = oPIndex(string)
    tree = stringToListWithNums(opIndex, string)
    opIndex2 = oPIndex(tree)
    opIndexSort = sortOps(tree,opIndex2)
    return crearArbol(tree, opIndexSort)
    

# Funcion que resuevel un arbol basico de un operador y dos hoja que son numeros
def solveBasicTree(tree):
    oP = tree[1]
    if oP == '+':
        return (tree[0] + tree [2])
    elif oP == '-':
        return (tree[0] - tree [2])
    elif oP == '*':
        return (tree[0] * tree[2])
    elif oP == '/' and tree[2] != 0:
        return (tree[0] / tree[2])
    else:
        return "Error operacion invalida"


# Funcion que busca sub arboles para resolver la cuacion
def solveTree(tree):
    index = 0
    while index <= len(tree)-1:
        if type(tree[index])  == list:
            tree[index] = solveTree(tree[index])
            index += 1
        else:
            index += 1
    return solveBasicTree(tree)


#funcion principal que llama a las demas funciones
def sovlveMathExp(string):
    return solveTree(getTree(string))

