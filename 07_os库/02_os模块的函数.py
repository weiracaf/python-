import os
import os.path

# os.listdir()
# 作用列出目录中所有文件以及目录，返回一个列表
print(os.listdir('D:/作业'))
# 错误写法但也可以输出print(os.listdir('D:\作业'))

# os.mkdir()创建一个目录（文件夹）
# 一次只能创建一个，不然会报错，且当对应目录有重名的文件夹，再次创建会报错
os.mkdir('D:/作业/python_os创建的文件夹')
# 前面的是对应想要在哪个目录创建，然后最后一个目录是我们要创建的
# （D:/作业）想在该路径创建(python_os创建的文件夹）这个文件夹

# rmdir()删除一个目录
# 一次删除一个，也是删除最后一个出现的目录
# 只能删除空文件夹不然会报错
os.rmdir('D:/作业/python_os创建的文件夹')


# os.makedirs()和os.removedirs()
# 递归创建目录和递归删除目录
# 创建智能识别
# 从第一个不存在的目录开始开始创建
os.makedirs('D:/学习/000/666/777')
# 如果输入的路径全都有，没有说不重名的，就会报错

os.removedirs('D:/学习/000/666/777')

# os.getcwd()
# 获取当前的工作目录
print(os.getcwd())

# rename()对文件或者目录进行重命名
# os.rename("D:/作业/院校列表.xlsx", "D:/作业/666.xlsx")
# 也可以发生对应文件格式转换，前提是格式要匹配，比如xlsx转docx什么的,灭找到对应文件，报错

# 针对系统的一些属性和方法

# os.sep
# 返回系统路径的分隔符，windows是\
print(os.sep)

# os.name
# 返回对应系统名字，windows返回nt
print(os.name)
