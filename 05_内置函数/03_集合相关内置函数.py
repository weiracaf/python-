set1 = {1, 2, 3, 4}

# 集合的重要特点，去重，可以把序列转集合，可以去掉序列中重复的元素

# 集合的添加和删除
set1.add(5)
print(set1)
set1.remove(5)  # 无，报错
print(set1)

if 5 in set1:
    set1.remove(5)
# pop方法会删除随机元素
set1.pop()
print(set1)

# clear()清空集合
set1.clear()
print(set1)

# del方法删除整个集合
del set1

# 集合的交并，差集运算
set2 = {1, 2, 3, 6}
set3 = {1, 4, 5, 2}
print(set2 & set3)  # 交
print(set2 | set3)  # 并
print(set2 - set3)  # 减
