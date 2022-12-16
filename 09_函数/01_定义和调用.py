# 定义函数形式
# def 函数名():
# 封装的代码
def say_hello():
    print('Hello')
    print('Hello')
    print('Hello')


def f_():
    global a  # a变成全局变量了，不过只在f_()函数内生效，就是其他函数调用a不是这个函数的a而是一个局部变量
    a = 100


def d_():
    a = 1000  # 这个a就是个局部变量


# 函数的调用
say_hello()
a = 10
f_()
d_()    # 这个相当于只改了自己的局部变量奥
print(a)  # 这里输出就是100喽
