# find（）  搜索指定字符串没有返回1
# rfind（） 从右边开始搜索
# index（） 搜索指定字符串，没找到报错
# rindex（）从右边开始搜索
# count（） 统计指定字符串出现次数
# 调用格式 str.find('b')
a = "a b c d e"
print(a.find('b'))
print(a.find('b', 3, 9))  # 指定区域搜索，初位置3，末位置9

# strip  去掉字符串两边的指定字符
# rstrip 去掉左边指定字符
# lstrip 去掉右边指定字符
# split（‘指定字符’，分隔次数）  以指定字符串分隔为列表
# 这些都是未指定字符串时，默认为空格
a = "a b c d e"
print(a.split())  # 默认不写的话，全分隔完，默认以空格分
print(a.split(' ', 1))
# upper 字符串所有都转为大写
# lower 字符串所有都转为小写
# swapcase 大转小，小转大
# capitalize 第一个字母变大写，其他小写
# title 以空格/换行隔开，字符串所有单词首个字母大写，其他小写
# 调用格式 a.upper(),不改变原字符串



# 字符串替换
# replace（‘old’，‘new’）所有old换为new
# replace（‘old’，‘new’，次数（int））多了一个次数


# 字符串拼接
# 字符c.join（可迭代对象）
# 代表以字符c为分隔符，将可迭代对象的元素一个个拿出来，拼接为字符串喽
li = ['1', '2', '3', '4', '5']
print(' '.join(li))
