import os
import sys

# CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]  # 当前目录
# config_path = CURRENT_DIR.rsplit('/', 1)[0]  # 上一级目录
# sys.path.append(config_path)
# print(config_path)

from tcp_lib.DAL.tcp_DAL import tcp_service

class Tcp_manager:

    def __init__(self):

        pass


    def init(self,addr,port):

      return tcp_service.init(addr,port)

    def get_socket(self):

        return tcp_service.get_socket()

    def tcp_addr_get(self):

        return tcp_service.tcp_addr_get()
    def tcp_port_get(self):

        return tcp_service.tcp_port_get()


    def change_addr(self,addr,port):
        tcp_service.change_addr(addr,port)

        pass
    def tcp_buffer_info(self):
     return tcp_service.tcp_buffer_info()

    def tcp_connect(self):
        return tcp_service.tcp_connect()

    def bind(self):
        pass

    def tcp_send(self, msg):
      tcp_service.tcp_send(msg)
    def resive(self):

       return tcp_service.resive()

    def tcp_close(self):
        tcp_service.tcp_close()

tcp_manager = Tcp_manager()
