import time


# 把辅助函数和主函数分隔开减少bug减少装饰器作用了
# 比如输入年龄，和判断年龄是否正常减少一个是主要功能函数，一个是辅助功能函数呗


def count(func):
    start = time.ctime()
    time.sleep(5)
    func()
    end = time.ctime()


def print1():
    for i in range(100):
        if i % 2 == 1:
            print(i)


count(print1)
# 就是把函数传给函数呗，实现两个函数的分离
