"""
测试同目录下py文件的导入问题
不做设置的时候，test4 和 User下面会有红线警告
但是此时代码是可以导入test4并且运行正常的
把红线弄没的方法是把当前文件夹 make directory as Source Root
然后就可以正常的使用了
"""
from test4 import User


if __name__ == '__main__':
    U = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    U.save()