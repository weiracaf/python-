# Python中的输入（input）
# 输出print()
print("告诉我你是谁")
name = input()
print("%s" % name)
# 上面的是最基本的input属于直接读取
# 但是这样先print提示太麻烦我们可以
# input(提示信息)，在输入内容前会先显示提示信息
print("%s" % input("请告诉我你是谁"))  # 和上面的其实是等价的


# 注意：input默认得到的都是字符串，想要得到数字需要自行强转
