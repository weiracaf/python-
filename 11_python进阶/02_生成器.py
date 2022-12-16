# 生成器是一种特殊的迭代器
# 生成器是自己生成元素给对象，从无到有的生成
ge = (2*i for i in range(3))
print(next(ge))
print(next(ge))
print(next(ge))     # 类似于列表推导式了

# yield关键字用于创建生成器


def wine():
    print('first yield')
    yield 1     # 程序运行到yield关键字，暂停，把yield后面的值结果返还给生成器作为第一个可迭代对象
    print('second yield')
    yield 2


a = wine()
print(next(a))
print(next(a))
a.close()  # 关闭生成器
