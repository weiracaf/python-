list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [6, 7, 3, 4, 5]
print(list1)
print(list2)

print(list1 + list2)  # 列表的合并（用+号）

print(list1 * 2)  # 列表重复继承来排成一个新的列表

# 列表的比较
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print(list3 == list4)
# 比较相等，只需要比较两个对象的内容是否相等，对象的内存地址可以不同

# 比较大小（>,<,>=,<=）
# 两个列表比较大小比较的是第一个不相等元素的大小，如果列表对应字母全相同，看长度，长度相同那就是相等了
list4 += [4]
print(list4 > list3)

# 元素 in/not in 列表
# 检查对应的元素是否在列表中存在/不存在
print(1 in list4)
print(list3 in [list4, [1, 2, 3]])  # 列表也可以作为元素，但是相对于的也必须是列表中的列表才行
# sum函数
# 对应的内部函数
# sum = 0
# for i in list3  #3中元素是123
#    sum += i
# return sum
print(sum(list3))  # 列表需无无字符串类型

# max,min
print(max(list3))  # 输出列表最大值
print(min(list3))  # 输出列表最小值

# len
# 返回列表的长度
print(len(list3))
print(len(list4))

# list.sort()和sorted(list)
# 两个都是排序的函数sort是对原列表直接操作，sorted是返回一个新列表
# sort无返回值，是None
# sorted作为一个内置函数，可以对所有课迭代对象进行排序
# print(list1.sort())报错
# 注意排序只能相同元素之间进行排序，不能说有字符串和数字你进行排序
print(sorted(list2))
print(list2)
list2.sort()
print(list2)

# 列表.append(x)只能添加一个
# 把元素x添加到列表末位，无返回值
# 先操作后输出
list3.append('a')
print(list3)

# extend可以添加多个元素不过参数是列表
list2.extend([1, 2])
print(list2)
list2.sort()
print(list2)
# insert(插入索引（从0开始喽），插入元素)插入
list5 = [1, 2, 4]
list5.insert(1, 3)
print(list5)
# pop(删除次序)删除列表对应次序的元素，且返回对应元素
print("删除的元素是" + str(list5.pop(1)))
print(list5)
# clear()清空
print(list5.clear())

# 列表.index(元素)索引
# 返回对应元素所在位置的索引
print(list2.index(1))
print(list2.index(2))

# 顺序相关函数
print("倒序前" + str(list3))
list3.reverse()
print("倒序后" + str(list3))

# 转换可以将元组转换为列表
tuple1 = (1, 2, 3)
print(tuple1)
print(list(tuple1))

# 复制
list6 = list3.copy()
print(list6 == list3)
# 感觉和直接赋值差不多啊


# 统计元素
# 列表.count(元素)
print(list3.count(1))  # 统计list3中1元素的个数

# 列表推导式

# [表达式 for 变量 in 列表 （if 条件）]

print([x*2 for x in list4])
print([x for x in list4 if x % 2])  # 输出全是奇数，2的整数倍条件表达式为0
