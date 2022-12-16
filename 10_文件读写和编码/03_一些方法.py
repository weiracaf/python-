with open('a.txt', 'r', encoding='utf-8') as f:
    num = 0
    while True:
        num += 1
        line = f.readline()     # readline()一行一行读取
        if line == '':
            break
        print(num, line)

with open('a.txt', 'r', encoding='utf-8') as a:
    m = a.readlines()   # readline 一行一行返回以列表形式存储
    print(m)
# 接下来是写入文件的操作
f = open('c.txt', 'w')
f.write('abc')
# 对应现在的文件夹生成一个c.txt

# writelines()传入一个序列，相当于把序列的元素一个个write，不会自动换行！,可以自己添加换行符
list1 = ['111\n', '222', '333', '444', '555']
f.writelines(list1)




