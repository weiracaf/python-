# 常见编码gbk编码，utf-8编码（最常用），Big5编码
# 编码就是把存储在内存的0和1按照你想按照的编码方式进行分割固定格式存取
# 编码转换
f = '你好'
c = f.encode('gbk')     # encode（编码格式），把调用的对象转换成对应的编码格式
print(f)
d = c.decode('gbk')     # decode（编码格式），把调用的对象以编码形式解包
print(d)

