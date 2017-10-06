# 装饰器的用法
import functools


# 修饰器 最外层是一个以函数func为参数的函数， 这个函数会返回把func函数修饰过后的函数wrapper，wrapper可以接受来自外层的参数
def log1(text):
    def decorator(func):
        def wrapper(*args, **kwargs):  # wrapper
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("1111111111111")
        return func(*args, **kwargs)
    return wrapper


@log2
def now(time):
    print("2017-10-6 %s" % time)


if __name__ == '__main__':
    now('14:28:00')
    print(now.__name__)  # 修饰后now的name变成wrapper，如果注释掉@log得到的是now
