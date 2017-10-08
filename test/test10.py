import types


@types.coroutine
def generator_coroutine():  # 这是生成器协程
    yield 1


async def native_coroutine():  # 这是原生协程
    await generator_coroutine()  # 原生协程是可以用await调用生成器协程的


def main():
    print(native_coroutine().send(None))  # 在非协程函数中用send()的方式来调用协程
    print(native_coroutine().send(None))


main()