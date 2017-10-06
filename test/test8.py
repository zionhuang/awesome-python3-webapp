# with的用法测试


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)

    def doSomething(self):
        a = 1/0
        return a

def getSample():
    return Sample()


if __name__ == '__main__':
    with getSample() as sample:
        sample.doSomething()
