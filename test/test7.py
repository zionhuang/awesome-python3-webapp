# python的参数类型


# POSITIONAL_OR_KEYWORD类型
def test1(a, b):
    print(a)
    print(b)


# VAL_POSITION 类型
def test2(*a):
    print(a)


# KEYWORD ONLY 类型
def test3(*, c):
    print(c)


# VAR_KEYWORD
def test4(**kwargs):
    print(kwargs)


# VAR_KEYWORD AND VAR_POSITION
def test5(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    test1('1','2')
    test1(b=2222,a=1111)  # 默认的 POSITIONAL_OR_KEYWORD 类型可以根据位置顺序和键值对来传参数
    test2(1,2,3)  # test2 是 VAR_POSITION 可以传入任意个数的参数进去，函数内的多个参数以元组的形式存在
    test3(c = 2232) # test3只能传键值对进出 不然会报错
    test4(a=1,b=2,c=3)  # 把参数打包成一个字典传到test4 中，不传参数或者不按关键字的方式传参数都会报错
    test5(1,2,3,4) # test5可以传入任意的参数和键值对
