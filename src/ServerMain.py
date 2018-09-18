import Server as s
import CheckSolution as check
import LightBot as lb
import threading
import os
import time
import serial

def get_mat():
    maze=[]
    maze = [[0]*8 for _ in range(8)]
    num_lights=0
    try:
        lb.main('prueba5.LBcc.txt')
    except Exception as e:
        print(e)
    from globalVar import _MAT as mat
    from globalVar import _POSSTART as pos

    i=0
    j=0
    for row in mat:
        for col in row:
            is_light = col.pop()
            maze[i][j]=col[0]
            if(is_light):
                maze[i][j]=(col[0]*10)+4
                num_lights+=1

            j+=1
        i+=1
        j=0
    return (maze, num_lights, tuple(pos))

def arduinoSendMoves(list_to_send):
    arduino = serial.Serial("COM3", 9600)
    time.sleep(2)
    for var in list_to_send:
        arduino.write(int_to_byte[var])
        rawString = arduino.readline()
        print(rawString)
        time.sleep(0.10)
    arduino.close()

def arduinoSendMaze(list_to_send):
    arduino = serial.Serial("COM3", 9600)
    time.sleep(2)
    i=0
    for row in list_to_send:
        for col in row:
            arduino.write(int_to_byte[col])
            rawString = arduino.readline()
            print(rawString)
            time.sleep(0.10)
            i+=1
    print(i)
    arduino.close()
    
def init_server():
    server.create_connection()

def listener():
    while True:
        if(server_thread.is_alive()==False):
            os._exit(0)
        elif(server.check_moves):
            moves=list(map(int, server.get_list()))
            time.sleep(0.1)
            if(len(moves)!=0):
                print(moves)
                test.reset_parameters()
                validated_moves=test.solvemaze(initial_pos[0], initial_pos[1], 0, 0, "DOWN", moves)
                validated_moves.insert(0, initial_pos[1])
                validated_moves.insert(0, initial_pos[0])
                if(test.win):
                    validated_moves.append(5)
                else:
                    validated_moves.append(6)
                print(validated_moves)
                try:
                    arduinoSendMoves(validated_moves)
                except Exception as e:
                    print(e)

moves=[]
server = s.Server()
test = check.CheckSolution()
int_to_byte = {0:b'0', 1:b'1', 2:b'2', 3:b'3', 4:b'4', 5:b'5', 6:b'6',
               8:b'8', 14:b'5', 24:b'6', 34:b'7'}

mat=get_mat()
test.maze=mat[0]
test.NUM_LIGHTS=mat[1]
initial_pos=mat[2]
#arduinoSendMaze(test.maze)
for row in test.maze:
    print(row)
    
server_thread = threading.Thread(target=init_server)
listener_thread = threading.Thread(target=listener)
server_thread.start()
listener_thread.start()
