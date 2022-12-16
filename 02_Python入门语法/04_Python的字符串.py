money = 10
a = str(money)
print(a)
print(type(a))

# 字符串的拼接
print("小袁" + "学计算机")  # 字面量间的拼接

print("小袁" + a + "个肝")  # 字面量和变量

# 字符串格式化
print("逆天%s" % a)
print("逆天%s%d" % (a, money))
