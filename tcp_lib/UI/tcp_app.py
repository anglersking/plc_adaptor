
from tcp_lib.BLL.tcp_BLL import tcp_manager


if tcp_manager.init('127.0.0.1',776):
    tcp_manager.tcp_buffer_info()
    tcp_manager.tcp_send('0x12 0x13 0x14 0x15 0x16')
    tcp_manager.resive()
    tcp_manager.tcp_close()
    tcp_manager.change_addr('127.0.1.1',777)
    if tcp_manager.tcp_connect():
        tcp_manager.tcp_send('0xff')
        tcp_manager.resive()
    else:
        pass

else:
    pass





