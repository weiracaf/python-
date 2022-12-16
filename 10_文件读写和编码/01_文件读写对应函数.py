import os
f = open("D:/作业/Demo.txt", 'r', encoding='utf-8')  # open函数open("路径(可以是相对于pycharm编译器位置，也可以是绝对路径)",“打开方式”)
print(f.read())
# 打开方式的话‘r’代表只读
# ‘w’代表只写
# ‘a’代表追加模式
# 对应的这基础三个字母可以与+和b和b+组合
# 例如wb w+ wb+ ab a+ ab+ r+ rb rb+ 都有不同的含义
# 自己查奥，懒得写了

# 对应打开的自然是关闭了
# 可以调用对应对象的closed属性来看文件是否关闭
print(f.closed)  # false的话就是没关闭
f.close()  # 这个就是关闭函数喽
print(f.closed)  # true就是关闭了呗


# 为什么要关闭，因为呗打开的文件是无法进行删除和重命名的


def rn():
    oldname = "D:\作业\测试.txt"
    newname = "D:\作业\Demo.txt"
    os.rename(oldname, newname)     # 不写绝对路径就是相对路径奥


# 上下文管理器,可以自动关闭文件
# with 文件名 as 变量:
# 语句
# 执行完同一个缩进的语句会自动关闭文件
# 如果上面都不想执行 可以写一个pass
with open('D:\作业\Demo.txt', 'r', encoding='utf-8') as a:
    print(a.read())
print('文件是否被关闭', a.closed)



