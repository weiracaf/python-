def f(a, b, c):
    print(a, b, c)
    return a+b+c


result = f(1, 2, 3)
print(result)
# 也可以返回多个值


def d(a, b, c):
    return a+b, b+c, a+c


e = d(1, 2, 3)
print(e)
# 以元组的形式返回奥
