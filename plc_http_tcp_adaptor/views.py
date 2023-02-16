import json

from django.http import HttpResponse
from django.shortcuts import render

import socket
import sys
from tcp_lib.BLL.tcp_BLL import tcp_manager


        
# # Create your views here.

def get_json(request):

    """获取非表单书据ｊｓｏｎ body raw
    测完
    """
    # 获取ｊｓｏｎ的书据
    datas_byt = request.body

    # 得到数据为ｂｙte需要转换
    datas = datas_byt.decode()

    print(datas)
    print(type(datas))
    dict_datas = json.loads(datas)


    print(dict_datas.get('cmd'))
    if(dict_datas.get('cmd')=='connect'):
        print("connect", dict_datas.get('addr'), )
        if tcp_manager.init(dict_datas.get('addr'), dict_datas.get('port')):
            tcp_manager.tcp_buffer_info()
            tcp_manager.tcp_send('0x12 0x13 0x14 0x15 0x16')
            # tcp_manager.resive()
            print("connect tcp ok")


    if (dict_datas.get('cmd') == 'close'):
        tcp_manager.tcp_close()

    if (dict_datas.get('cmd') == 'change_tcp'):
        tcp_manager.tcp_close()
        tcp_manager.change_addr(dict_datas.get('addr'), dict_datas.get('port'))
        if tcp_manager.tcp_connect():
            print("change and reconnect tcp ok")

    if (dict_datas.get('cmd')=="send"):
        print("send->",dict_datas.get('value'),"convert_tcp")
        tcp_manager.tcp_send(dict_datas.get('value'))
        print("tcp_convert and send ok...,")
    if (dict_datas.get('cmd') == "send"):
        print('I have recive ',tcp_manager.resive())


    return HttpResponse('status_ok')



