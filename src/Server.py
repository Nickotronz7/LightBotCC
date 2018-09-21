import socket
import sys

##################################
#Clase servidor
#Conecta con la aplicación y retorna los movimientos
#del usuario
##################################

class Server:
    HOST = socket.gethostname()
    PORT = 8888
    moves=""
    check_moves = False

    def set_list(self, _list):
        _list = list(str(_list[1:-2], 'ascii'))
        for var in _list:
            if(var==','):
                _list.remove(var)
        self.moves = _list
        self.check_moves = True

    def get_list(self):
        self.check_moves = False
        return self.moves

    def create_connection(self):
        moves_aux=""
        print("TU DIRECCION IP ES:",socket.gethostbyname_ex(socket.gethostname()))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')
 
        try:
            s.bind((self.HOST, self.PORT))
        except socket.error as err:
            print('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
            sys.exit()
 
        print('Socket Bind Success!')
 
        s.listen(10)
        print('Socket is now listening')
        conn, addr = s.accept()
        print('Connect with ' + addr[0] + ':' + str(addr[1]))

        i_empty_list=0
        while True:
            buf = conn.recv(128)
            moves_aux=buf
            if(moves_aux!=""):
                self.set_list(moves_aux)
                if(self.moves==[]):
                    i_empty_list+=1
                    if(i_empty_list==3):
                        s.close()
                        print("\n"+"Socket close"+"\n")
                        break
