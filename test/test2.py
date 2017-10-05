import asyncio


def B():
    a = 0
    b = 0
    while True:
        a = yield b
        b += a


def A(b):
    b.send(None)
    for i in range(1, 4):
        try:
            print(b.send(i))
        except:
            return


b = B()
b.send(None)
print((b.send(1)))


# async def hello(n):
#     print("hello world %s" % n)
#     r = await asyncio.sleep(n)
#     print("hello again %s" % n)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [hello(1), hello(2), hello(10)]  # 输出结果总是不能和任务的顺序相同
#     loop.run_until_complete(asyncio.wait(tasks))  # 把任务放到loop里面去执行，执行完了就退出
#     loop.close()


# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)  # open_connection 也是一个一个coroutine，所以也是一个生成器
#     reader, writer = yield from connect  # yield from 后面接一个可迭代的对象， 这里可以理解为它只是得到了 writer和reader
#     print(type(reader))
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' %host
#     writer.write(header.encode('UTF-8'))
#     while True:
#         line = yield from reader.readline()  #这里的IO操作才是我们
#         yield from asyncio.sleep(1)
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio
#
# from aiohttp import web
#
#
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>', content_type='text/html')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'), content_type='text/html')
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()


