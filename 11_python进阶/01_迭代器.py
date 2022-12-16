# 迭代器，用于遍历可迭代对象
# 可迭代对象类似于序列，元组等
list1 = [1, 2, 3]
it = iter(list1)
print(it)
print(next(it))     # next方法用来取下一个迭代对象，最开始是0第一次调用就是第一个对象呗
print(next(it))
print(next(it, 'e'))
print(next(it, 'e'))    # 后面那个参数其实就是在你没迭代对象的话最后输出的

# 其实增强for循环结束一个调用迭代器的过程


