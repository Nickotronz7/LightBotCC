global _MAT
_MAT = []

global _POSSTART
_POSSTART = [0,0]

global _ACTUALPOS
_ACTUALPOS = [0,0,1] # X, Y, Side

def printMat():
	global _MAT
	for i in range(0,8):
		print(_MAT[i])

global _VARIABLES
_VARIABLES = {}

global _SWITCH
_SWITCH = {
			0:[0,-1],
			1:[0,1],
            2:[1,0],
			3:[-1,0]
		}