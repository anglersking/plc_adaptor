import os
import sys
#
# CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]  # 当前目录
# config_path = CURRENT_DIR.rsplit('/', 1)[0]  # 上一级目录
# sys.path.append(config_path)
# print(config_path)
import  socket
from tcp_lib.MODEL.tcp_model import tcp
class Tcp_service:
    def __init__(self):
        self.s=None
        pass


    def init(self,addr,port):

        tcp.addr=addr
        tcp.port=port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        failed_count = 0
        while True:
            try:

                print("start connect to server ")
                print(self.tcp_addr_get(),self.tcp_port_get())
                addr_reality=self.tcp_addr_get()
                port_reality=self.tcp_port_get()
                self.s.connect((addr_reality,port_reality))

                print("init sucess!")
                break
            except socket.error:
                failed_count += 1
                print("fail to connect to server %d times" % failed_count)
                if failed_count == 10: return False

        return True

    def get_socket(self):

        return self.s

    def tcp_addr_get(self):

        return tcp.addr
    def tcp_port_get(self):

        return tcp.port


    def change_addr(self,addr,port):
        tcp.addr=addr
        tcp.port=port
        pass
    def tcp_buffer_info(self):
        # get the socket send buffer size and receive buffer size
        s_send_buffer_size = self.get_socket().getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        s_receive_buffer_size = self.get_socket().getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

        print("client TCP send buffer size is %d" % s_send_buffer_size)
        print("client TCP receive buffer size is %d" % s_receive_buffer_size)

        return s_send_buffer_size, int(s_receive_buffer_size)
    def tcp_connect(self):
        # send and receive
        print("connecting...")
        if self.init(self.tcp_addr_get(),self.tcp_port_get()):
            print("connect success!")
            return True
        else:
            return False

    def bind(self):
        pass

    def tcp_send(self, msg):
        # msg = 'hello server, i am the client'
        print(msg.encode('utf-8'))

        self.get_socket().send(msg.encode('utf-8'))
        print("send len is : [%d]" % len(msg))
        pass
    def resive(self):

        msg = self.get_socket().recv(1024)
        print(msg.decode('utf-8'))
        print("recv len is : [%d]" % len(msg))
        return msg,len(msg)

    def tcp_close(self):
        self.get_socket().close()

tcp_service = Tcp_service()
