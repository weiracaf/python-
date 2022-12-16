a = 5
b = 3
if a > b:
    print("牛牛牛")
    print("判别式的条件正确")
else:
    print("不行")
    print("判别式的条件错误")
print("该行缩进不同和不在else的作用域里哦")

# Python没有自增和自减运算符（++和--）

if a > b:
    print("a>b")
elif a < b:  # elif相当于else if的缩写
    print("a<b")
else:
    print("a=b")
