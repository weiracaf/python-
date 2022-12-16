# 逻辑运算符
print(1 and 0)  # and相当于其他语言的&&（和）
print(1 or 0)  # or相当于其他语言的||（或）
print(not 0)  # not相当于其他语言的！（非）

# 身份运算符is is not  类似于java中的equals()来判断是否是同一个对象
a = 100
b = 100
print(a is b)  # 注意:python中常量地址是同一个的对应的变量名所指向都是同一个地址，所以这个结果应该是True
c = 10
print(a is not c)

# 取址操作id()
a = 1  # 相当于重新赋值
b = 1
print(id(a), id(b))
print(id(a) == id(b))

# 成员运算符in    not in
# 用来判断对象是否在对应的序列（可以包含不同数据类型的排列）in 存在返回true 不存在返回false，not in相反
x = [1, 2, [1, 2]]

