import socket

def echo():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#sock_stream流式套接字不能选和protocol的udp结合
    sock.bind(('127.0.0.1',5555))#(把一个地址族中的特定地址赋给socket，和端口号）一般只有服务端的才要bind，这是一个各个client都欢迎访问的
    sock.listen(10)#进行监听，将创建的socket从主动类型变成被动类型
    while True:
        conn,address = sock.accept()#tcp的第三次握手在此完成，获得了conn（新的接套字对象可以接收和发送对象和客户端的ip+port），conn是用来read和write的
        while True:
            data = conn.recv(2048)#一有数据就返回但是最大的长度就2048
            if data and data != b'exit\r\n':#有数据，并且数据不为exit
                conn.send(data)
                print(data)
            else:
                conn.close()
                break
if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass