import re
# re.findall()
# 搜索返回所有能匹配到的子串，返回对象为列表
re.findall(r'想要找的字符串', '源字符串')

# re.match()
# 从字符串开头进行匹配，返回类型为match对象（只能从头开始，如果源字符串开头的第一个字母和对应的匹配的第一个字母不同，报错）通过re.search()解决
# 只能匹配到一个对象
a = 'python123123145a'
print(re.match('python', a))
# 通过match对象的group方法能获取到具体匹配的字符串(好像是还没通过正则转义的字符串)


# re.search()
# 搜索匹配到的第一个位置，返回类型为match对象
# 也是只能匹配到一个对象
a = 'python123123145a'
print(re.search('1', a).group())
print(re.search('1', a))  # 1有3个不过只输出第一个

# 如果你想匹配多个的话用findall()


# match中的group方法
print("下面到group奥")
c = '123abc456'
print(re.search(r'\d+', c).group())     # 懂没？，group(0)是返回对应拼接的字符串，group(1)返回第一个（）括住的元素，单独group(2)的第二个()里的元素喽
# 默认如果你不写参数输出的是match.group(0)
print(re.search(r'\d+', c).group(0))
print(re.search(r'(\d+)(a)', c).group(1))  # 注意看哦，我这里给我的\d+变成了(\d+),这就代表有组了
print(re.search(r'(\d+)(a)(b)', c).group(0))  # 然后我可以向组里添加多个元素来进行匹配，这样可以把匹配的结果分开来，不过还是匹配一个完整的字符串
# 一般配合正则表达式的转义字符配合找对应的匹配出来的字符
print(re.search(r'(\d+)(a)(b)', c).groups())  # 以元组的形式返回各组




# re.split()
# 字符串按照匹配的结果进行分割，返回为列表类型
# 参数：分割字符，源字符串，最大分割次数
# 最大分割次数可以不写代表不限制
print(re.split('1', '22221333314444', 1))
print(re.split('1', '22221333314444'))


# re.finditer()
# 与findall类似，在字符串中找到正则表达式所匹配的子串，并把它们作为一个迭代器返回
# findall是一个列表finditer是返回迭代器
num = '12a32bc43jf3'
it = re.finditer(r'\d+', num)
for match in it:
    print(match.group())


# re.sub()
# 在字符串中替换所有匹配正则表达式的子串，返回替换后的字符串，返回类型为字符串
# sub('','',int )第一个正则表达式，第二个是源字符串，第三个是最大替换次数（可以不写和split那个相同）


# re.compile(正则表达式)，返回一个对象的模式
# 然后这个模式可以直接匹配字符串很方便
# 限于你想多次匹配某一种类型正则表达式
a = re.search(r'\d+', '100816a')

regex = re.compile(r'\d+')
b = regex.search('100816a')
print(a)
print(b)
# 可以发现奥第一种适合于只匹配一次
# 第二种适合于你想多次匹配那个正则表达式，match(),findall()等等都可以用

