import Server as s
import CheckSolution as check
import threading
import os
import time

server = s.Server()
test = check.CheckSolution()
moves=[]
win=False

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
                win=test.solvemaze(0, 0, 0, 0, "DOWN", moves)
                test.win=False
                print(win)

server_thread = threading.Thread(target=init_server)
listener_thread = threading.Thread(target=listener)
server_thread.start()
listener_thread.start()
