import socket
import sys


HOST=socket.gethostname()
PORT = 8888
moves=""

def set_list(_list):
    _list = list(str(_list[1:-2], 'ascii'))
    for var in _list:
        if(var==','):
            _list.remove(var)
    return _list
            

def create_connection():
    #print("TU DIRECCION IP ES:",socket.gethostbyname_ex(socket.gethostname()))
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket created')
 
    try:
        s.bind((HOST, PORT))
    except socket.error as err:
        print('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
        sys.exit()
 
    print('Socket Bind Success!')
 
    s.listen(10)
    print('Socket is now listening')
    
    while True:
        conn, addr = s.accept()
        print('Connect with ' + addr[0] + ':' + str(addr[1]))
        buf = conn.recv(128)
        moves=buf
        if(moves!=""):
            break
    s.close()
    print("\n")
    return set_list(moves)
