# for循环格式 for 自定义变量 in 可循环变量
a = [0, 2, 3]
for b in a:  # 相应序列
    print(b)
for b in range(2):  # range（2）指的是在0-1范围，从0开始n个数字，用来控制循环的次数
    print("你好")

# while循环
# while 条件表达式:
# 代码块
while a[0] < 9:
    print(a[0])
    a[0] += 1
