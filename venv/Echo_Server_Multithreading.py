import socket,threading

class Echo(threading.Thread):#这两个类的关系属于dependency，没有建立实例，直接调用
    def __init__(self,conn,address):
        threading.Thread.__init__(self)
        self.conn = conn
        self.address = address

    def run(self):
        while True:
            data = self.conn.recv(2048)
            if data and data !=b'exit]r\n':
                self.conn.send(data)
                print('{} sent: {}'.format(self.address,data))#用来显示数据和数据源
            else:
                self.conn.close()
                return
def echo():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',5555))
    sock.listen(1)
    while True:
        conn,address = sock.accept()
        Echo(conn,address).start()#start() start the threading activity ,it will arrange the run()
if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass