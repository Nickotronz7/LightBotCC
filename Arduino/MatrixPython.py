import serial
import time
import random

ser = serial.Serial('COM3', 9600, timeout = 0)

counter = 0

time.sleep(1)

matrix1 = [0,1,0,1,2,3,2,0,
           0,1,0,1,2,7,6,0,
           8,8,8,8,8,8,4,0,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8]

matrix2 = [0,0,0,0,0,0,0,0,
           1,1,1,1,1,1,1,1,
           2,2,2,2,2,2,2,2,
           3,3,3,3,3,3,3,3,
           4,4,4,4,4,4,4,4,
           5,5,5,5,5,5,5,5,
           6,6,6,6,6,6,6,6,
           7,7,7,7,7,7,7,7]

matrix3 = [8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,0,0,0,4,4,4,8,
           8,1,1,1,5,5,5,8,
           8,2,2,2,6,6,6,8,
           8,3,3,3,7,7,7,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8]

player1 = [0,0,1]

player2 = [3,4,3]

matrix10 = ''.join(str(e) for e in matrix1)
matrix20 = ''.join(str(e) for e in matrix2)
matrix30 = ''.join(str(e) for e in matrix3)
player10 = ''.join(str(e) for e in player1)
player20 = ''.join(str(e) for e in player2) 


time.sleep(1)

matrix = matrix20
#player = player10

ser.write(matrix.encode())
#ser.write(player.encode())
print(matrix.encode())
#print(player.encode())
 

