# lambda是没有函数名字的函数，
# 没有函数名子调用呢


f = lambda a, b: print(a + b)
f(1, 2)  # 1.赋值给一个变量
(lambda a, b: print(a + b))(1, 2)  # (lambda函数)（参数）相当于直接调用


def f():
    return lambda x, y:print(x + y)


a = f()
a(1, 2)
# 方式3将lambda作为返回值，本质上还是第一种方法，赋值变量的操作
