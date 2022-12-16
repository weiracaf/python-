import copy  # 先导入相应的包
# 深浅拷贝是相对于对象而言的，所以我们创建一个序列对象来完成相应操作

a = [1, 2, 3, [4, 5, [6, 7]]]


# 直接赋值（=） copy() 和copy.deepcopy()三者间区别


# =
b = a
print(id(a))
print(id(b))
print(id(b) == id(a))  # 这里的运行结果是True，说明a直接赋值给b，相对于把b也指向了a指向的区域

# copy
b = copy.copy(a)  # 也可以用a.copy()

print(id(b) == id(a))  # 这里是False，然后我们具体分析一下吧
b[0] = 2
print(b)
print(a)  # 这里b改变没有改变a对象的值
b[3][1] = 6
print(b)
print(a)  # 这里b的改变改变了a的内对象的值

# copy.deepcopy()

a = [1, 2, 3, [4, 5, [6, 7]]]

b = copy.deepcopy(a)

print(id(b) == id(a))  # 这里是False，然后我们具体分析一下吧
b[0] = 2
print(b)
print(a)  # 这里b改变没有改变a对象的值
b[3][1] = 6
print(b)
print(a)  # 这里b改变没有改变a对象的值
# 所以深拷贝无论如何新的对象改变对应旧对象没有任何影响
# 下面我们来看对应内存中的变化
