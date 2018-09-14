import Server as s
import CheckSolution as check
import threading
import os
import time
import serial

moves=[]

server = s.Server()
test = check.CheckSolution()

int_to_byte = {0:b'0', 1:b'1', 2:b'2', 3:b'3', 4:b'4'}

def arduinoConnection(list_to_send):
    arduino = serial.Serial("COM4", 9600)
    time.sleep(2)
    for var in list_to_send:
        arduino.write(int_to_byte[var])
        rawString = arduino.readline()
        print(rawString)
        time.sleep(0.25)
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
                validated_moves=test.solvemaze(0, 0, 0, 0, "DOWN", moves)
                print(validated_moves)
                try:
                    arduinoConnection(validated_moves)
                except Exception as e:
                    print(e)


server_thread = threading.Thread(target=init_server)
listener_thread = threading.Thread(target=listener)
server_thread.start()
listener_thread.start()
