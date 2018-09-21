import socket

hello = [b'HTTP/1.0 200 OK\r\n',
         b'Connection: close'
         b'Content - Type:text/html;charset=utf-8\r\n',
         b'\r\n',
         b'<html><body>Hello World!<body></html>\r\n',
         b'\r\n']
err404 = [b'HTTP/1.0 404 Not Found\r\n',
          b'Connection: close'
          b'Content - Type:text/html;charset = utf-8\r\n',
          b'\r\n',
          b'<html><body>404 Not Found<body></html>\r\n',
          b'\r\n']

def web():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8080))
    sock.listen(10)#listen里传的参数相当于是socket的耳朵数。一个耳朵探测一个可能的客户端连接。如果一个与客户端的连接已经建立，那么这个耳朵就腾空了。潜在监听能力还是10。This line has the server listen for TCP connection requests from the client. The parameter specifies the maximum number of queued connections
    while True:
        conn,address = sock.accept()
        data = conn.recv(2048).decode().split('\r\n')
        print(data[0].split(' '))
        res = err404
        if data[0].split(' ')[1] == '/':
            res = hello
        for line in res:
            conn.send(line)
        conn.close()

if __name__ == "__main__":
    try:
        web()
    except KeyboardInterrupt:
        pass