def consumer():
    r = ""
    while True:        
        n = yield r
        print("n = %s" %n)
        if not n:
            return  # 这里这句话不会被执行，因为初始化的时候r是空字符串返回给produce并被挂起，回来的时候send已经传来
            #         也就是说，yield的时候，‘n =’ 也没有执行，当外部send值进来的时候，n = send进来的值，所以n还没有机会等于空字符串
        print("consumer %s" %n)
        r = "200 OK"            


def produce(s):
    s.send(None)  # 初始化生成器，yield r 执行完并且挂起，这里的r = ""
    n = 0
    while n<5:
        n += 1
        print("produce %s" %n)
        r = s.send(n)
        print("consumer return %s" %r)
    s.close()


s = consumer()
produce(s)