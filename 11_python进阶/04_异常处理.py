# 异常是python一种对象类型
# 可以捕获处理/抛出
# 类似java中的呗
# open('123.txt', 'r')        # 没有对应文件报错

try:            # try用来捕获异常包含对应缩进的代码如果出现异常会跳到expect找对应错误类型，进行处理，如果没有对应异常类型，还是报错停止
    open('123.txt', 'r')
    a = 0
    print('1')
    b = 1
    c = b/a
except FileNotFoundError:       # expect 后面放的就是异常类型奥，也可以使用多个expect
    print("我不到啊")
except ZeroDivisionError:
    print("分母不能为0")
print('?')
# 还有try expect else当没有异常的时候最后会运行else最后的语句
# try finally无论有没有finally后面程序都运行一遍


# 抛出异常用raise
