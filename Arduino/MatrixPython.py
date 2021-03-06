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

matrix4 = [1,2,3,4,5,6,7,8,
           2,3,4,5,6,7,8,1,
           3,4,5,6,7,8,1,2,
           4,5,6,7,8,1,2,3,
           5,6,7,8,1,2,3,4,
           6,7,8,1,2,3,4,5,
           7,8,1,2,3,4,5,6,
           8,1,2,3,4,5,6,7]

matrix5 = [0,0,8,8,8,8,8,8,
           8,0,8,8,8,8,8,8,
           8,4,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8]
           

player1 = [0,0]
player2 = [2,4]

command1 = [2,2,2,2,2]
command2 = [2,1,4,1,2,4,2,1]
command3 = [0,2,3,0,3,3,3,4,0,4,1,0,4,9]
command4 = [2,0,1,0,0,4,4,4,4,4,4,4]


matrix10 = ''.join(str(e) for e in matrix1)
matrix20 = ''.join(str(e) for e in matrix2)
matrix30 = ''.join(str(e) for e in matrix3)
matrix40 = ''.join(str(e) for e in matrix4)
matrix50 = ''.join(str(e) for e in matrix5)

player10 = ''.join(str(e) for e in player1)
player20 = ''.join(str(e) for e in player2)

command10 = ''.join(str(e) for e in command1)
command20 = ''.join(str(e) for e in command2)
command30 = ''.join(str(e) for e in command3)
command40 = ''.join(str(e) for e in command4)  


matrix = matrix10
pos = player10
command = command30


matrixPart1 = matrix[:32]
matrixPart2 = matrix[32:]


time.sleep(1)


ser.write(matrixPart1.encode())
time.sleep(1)
ser.write(matrixPart2.encode())
time.sleep(1)
ser.write(pos.encode())
time.sleep(1)
ser.write(command.encode())

print(matrixPart1)
print(matrixPart2)
print(pos)
print(command)

 

