# key-value字典
cat = {'name': 'petter', 'color': 'black', 'size': 'fat'}
print(cat)  # 可以直接输出字典
# 生成字典
# 字典的直接定义
cat = {'name': 'petter', 'color': 'black', 'size': 'fat'}
# dict()函数生成字典,zip(list,tuple)都可以可以两个列表或者穿插或者两个元组
key = ('yi', 'er', 'san')
value = [1, 2, 3]
zip1 = zip(key, value)  # 转化为zip对象
print(dict(zip1))
# 特殊字典创建,输出格式不同
key1 = ('1', '2', '3')
value = ['yi', 'er', 'san']
word = {key1: value}
print(word)
# 空字典
word = {}
# 值为空的字典,fromkeys函数
key1 = [1, 2, 3, 4]
d = dict.fromkeys(key1)
print(d)
# 删除字典del函数
del d[1]  # 删除【】内部对应字典的key
print(d)
del d  # 删除整个字典
# 清空字典
word.clear()
print(word)

# 获取对应的值
score = {'1': 67, '2': 88, '3': 89}
print(score['1'])  # []里写对应的键（key），可以得到对应的value，但是如果不存在会报错
# 我们可以用下面这种方式防止错误发生导致整个程序停止
print(score[1] if 1 in score else "字典里没有对应结果")  # 这里的结果应该是没有，因为我输入的整数1
print(score.get('1'))  # 通过key直接求value，好用

# 遍历字典
# item(),keys(),values(),分别取的是对应的键值对，键，值
cat = {'name': 'petter', 'color': 'black', 'size': 'fat'}
for item in cat.items():
    print(item)
for value8, key8 in cat.items():
    print(key8, '对应的是', value8)
for item in cat.keys():
    print(item)
for item in cat.values():
    print(item)

# 更改和删除字典元素
# 语法为dic[key]=value

# 删除字典元素语法，防止报错
# if ‘is’ in dic：  没有的话会报错
# del dic['is']

# 字典推导式
# 键表达式：值表达式for循环
# 求1到10（键）每个数的平方
d1 = {i: i**2 for i in range(1, 11)}
print(d1)
