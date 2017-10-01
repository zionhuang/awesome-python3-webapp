def consumer():
    r = ''
    while True:
        n = yield r  # 每次n把值传进来，执行下面的操作，然后循环回来把值传出去
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 初始化生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 把值传给生成器
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
