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
           8,0,0,0,0,0,0,8,
           8,1,1,1,1,1,1,8,
           8,2,2,2,2,2,2,8,
           8,3,3,3,3,3,3,8,
           8,8,8,8,8,8,8,8,
           8,8,8,8,8,8,8,8]

while (counter < 64):
    
    toprint = str(matrix2[counter])
    printing = toprint.encode()
    ser.write(printing)
    print(counter ,printing, counter%8, counter//8)
    counter += 1
    time.sleep(0.5)
              

