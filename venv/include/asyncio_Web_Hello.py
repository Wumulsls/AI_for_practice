import asyncio#异步io，协程中的一种

async def dispatch(reader,writer):
    while True:
        data = await reader.readline()#暂停协程的执行，来等待某协程的完成
        message = data.decode().split(' ')
        print(data)
        if data == b'\r\n':
            break
    writer.writelines([
        b'HTTP/1.0 200 OK\r\n',
        b'Content-Type:text/html; charset=utf-8\r\n',
        b'Connection:close\r\n',
        b'\r\n',
        b'<html><body>Hello World!<body></html>\r\n',
        b'\r\n'
    ])
    await writer.drain()
    writer.close()

"""__name__ == '__main__' 当运行.py文件的时候会直接运行这个之下的代码，而导入该文件中的其他模块的时候不会运行该行代码之下的代码"""
"""__name__是一个内置变量，用于表示当前的模块名和包结构"""
if __name__ == '__main__':#当一个.py被直接运行的时候没有包结构，__name__就会 = __main__
    loop = asyncio.get_event_loop()#创建一个事件循环
    coro = asyncio.start_server(dispatch,'127.0.0.1',8080,loop=loop)#创建了一个服务器协程
    server = loop.run_until_complete(coro)#将协程注册到事件循环上

    #Server requests until Ctrl+C is pressed

    print('Server on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    #close the server
    server.close()#close the server first then close the loop event，because we put the asyncio server on the loop event
    loop.run_until_complete(server.wait_closed())#等循环上的server关掉
    loop.close()#再把循环关了