import os
import os.path

# 可以把os.path认为是一个处理带有'/'或者'\'字符串的一个工具
# 操作类函数
# os.path.split()
print(os.path.split('/python/demo/test.py'))
# 找到字符串最后一个\或者/把两端的字符串分隔，以元组的形式返回

# os.path.join()相当于合并两个字符串中间填上/或者\(不同系统添加不同)
# windows-\,linux-/
print(os.path.join('/hello', 'good/boy'))

# os.path.splitext()
# 和上面的os.path.split()差不多，只不过最后的分隔符变成了.（就是这个点）

# os.path.dirname()
# 提取上一层目录,以对应的斜杠或者反斜杠为分隔符
path = '/py/demo/test'
print(os.path.dirname(path))

# 转换类函数
# abspath()返回对应文件的绝对路径，空字符串返回当前工作文件所在目录
print(os.path.abspath(''))
print(os.path.abspath('.'))  # 一个点也是返回当前工作目录
print(os.path.abspath('..'))  # ..是返回当前工作目录的上一级目录

# normpath()
# 作用：规范、格式化路径，会把路径分隔符按照操作系统进行替换，也会删除一些冗余分隔符
path = '/home//user/d'
print(os.path.normpath(path))  # 这里会删除多余的分隔符/，并且把这些分隔符全改为\
path1 = '/home/him/../d'  # 因为..代表是返回上一级目录的意思奥，所以格式化后，..和他前面以及目录都会消失
print(os.path.normpath(path1))
path = '/./11/22'
# /.会直接删除，应为这个代表当前文件夹，但是不说也是当前文件夹
print(os.path.normpath(path))

# 判断类函数
# exists()判断当前路径是否存在，该参数可以是相对路径或者绝对路径
print(os.path.exists('D:/作业'))
# 当是相对路径时是相对于现在这个文件工作的目录而言的
print(os.path.abspath('.'))
print(os.path.exists("../../作业"))  # 当前工作文件夹返回两次才是d盘

# os.path.isfile（路径/文件名）/（文件名）
# 作用判断对应路径是不是一个文件，如果直接写文件名，会在当前工作区域内找该文件

# os.path.isdir(目录)
# 判断给定的字符串是不是在当前电脑上的一个目录

# os.path.isabs()
# 判断输入的字符串是不是一个绝对路径的格式，不存在判断对应路径存不存在当前电脑
print(os.path.isabs("C:/666/777/888"))

