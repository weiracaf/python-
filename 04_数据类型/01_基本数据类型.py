# 整形 int
n1 = 90
n2 = 0b10101111
print('十进制数', n1, type(n1))
print('二进制数', n2, type(n2))
# 浮点型 float
n1 = 1.1  # 1.0001100...
n2 = 2.2  # 110.0011...
n3 = 2.1
print(n1+n2)  # 浮点数的储存和运算具有不确定性，应为浮点数在计算机二进制储存，都是先转换二进制然后计算
print(n1+n3)  # 这个输出就是精确的
# 布尔类型 bool
a = 4 > 9
b = 9 > 4
print(a, type(a))
print(b, type(b))
# 字符串 str
a = 'str'
b = "I am a student"
c = '''lei
    bu lei'''  # 双引号单引号三引号都ok
# 我们想要字符串里有单引号，就用双引号定义，双引号同理
# 三引号可以定义多行字符串
print(a, type(a))
print(b, type(b))
print(c, type(c))
# 列表 内置可变有序序列，列表中的元素可以不相同，可以同时包含多种类型（基本所有数据类型都可以）(包含列表本身)，用[]界定
a = [1, 2, 3.3, "老鼠爱大米", [1, 1, 1]]
print(a)
# 元祖 有序 不可变 序列，可看为轻量级的列表，比列表功能简单，形式上接近，不过用()界定
# 注意：不可变
a = ('a', 3, [1, 2])
print(a)
# 字典 包含若干 键：值（key:value）对的无序可变序列, "键"和“值”定义中间用：隔开，相邻元素逗号隔开，用{}进行界定，键不能重复
a = {'name': 'LiMing', 'age': 27, 'name': 'xiaoyuan'}
print(a)
# 集合（set） 和字典差不多，就是把字典的value值全换为一个固定值，我们只输出key
a = {'apple', 'banana', 'cherry', 'cherry'}
print(a)