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

matrix3 = [0,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8,
           8,0,4,5,6,7,2,8,
           8,1,1,1,1,1,1,8,
           8,1,1,1,1,1,1,8,
           8,3,3,3,3,3,3,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8]

matrix10 = ''.join(str(e) for e in matrix1)
matrix20 = ''.join(str(e) for e in matrix2)
matrix30 = ''.join(str(e) for e in matrix3) 


time.sleep(1)

matrix = matrix30

ser.write(matrix.encode())
print(matrix.encode())
 

