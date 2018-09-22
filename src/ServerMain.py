import Server as s
import CheckSolution as check
import LightBot as lb
import threading
import os
import time
import serial

##################################
#Recibe la matriz generada por el analizador
##################################
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


#Envía los datos necesarios al arduino
def arduinoSendMoves(list_to_send):
    arduino = serial.Serial("COM5", 9600)
    time.sleep(2)
    arduinoSendMaze(cutMatrix(test.maze), arduino)
    list_=cutMatrix(list_to_send)
    position = list_[:2]
    moves = list_[2:]
    arduino.write(position.encode())
    time.sleep(1)
    arduino.write(moves.encode())
    arduino.close()
    

def arduinoSendMaze(list_to_send, arduino):
    matrix1 = list_to_send[:32]
    matrix2 = list_to_send[32:]
    print(matrix1)
    print(matrix2)
    arduino.write(matrix1.encode())
    time.sleep(1)
    arduino.write(matrix2.encode())

def cutMatrix(maze):
    str_maze=str(maze).replace("[", "")
    str_maze=str_maze.replace("]", "")
    str_maze=str_maze.replace(",", "")
    str_maze=str_maze.replace("14", "5")
    str_maze=str_maze.replace("24", "6")
    str_maze=str_maze.replace("34", "7")
    str_maze=str_maze.replace(" ", "")
    return str(str_maze)
    
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
                    validated_moves.append(9)
                print(validated_moves)
                try:
                    arduinoSendMoves(validated_moves)
                except Exception as e:
                    print(e)

                    
##################################
#MAIN
##################################
                    
moves=[]
server = s.Server()
test = check.CheckSolution()
int_to_byte = {0:b'0', 1:b'1', 2:b'2', 3:b'3', 4:b'4', 5:b'5', 6:b'6',
               8:b'8', 9:b'9', 14:b'5', 24:b'6', 34:b'7'}

    
mat=get_mat()
test.maze=mat[0]
test.NUM_LIGHTS=mat[1]
initial_pos=mat[2]

arduino = serial.Serial("COM5", 9600)
time.sleep(2)
arduinoSendMaze(cutMatrix(test.maze), arduino)
arduino.close()

for row in test.maze:
    print(row)

#Hilos creados con el fin de interactuar con el cliente y el servidor
#de manera independiente
server_thread = threading.Thread(target=init_server)
listener_thread = threading.Thread(target=listener)
server_thread.start()
listener_thread.start()


