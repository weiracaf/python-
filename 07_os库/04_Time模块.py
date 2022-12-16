import time
print(time.time())
# 获取当前时间戳，时间戳是从1970年1月1日凌晨到当前时间的总秒数
# 机器能看懂

print(time.localtime())
# 时间元组(struct_time)
# 返回一个元组对应索引位置元素代表年，月，日，时，分，秒，星期，儒略日，夏时令

# 时间字符串就是人能看懂的字符串，给人看的

# 其他两种只能与时间元组之间相互转换奥

# 三种格式互相转换
# 1.时间戳转为时间元组
# localtime，这个对应北京时间
print(time.localtime(time.time()))  # 不写参数默认也是这样
# gmtime(时间戳),这个表示是对应的0时区
print(time.gmtime())
print(time.gmtime(time.time()))  # 上下两个不写参数都一样喽

# 2.时间元组转字符串时间
print(time.strftime('%Y-%m-%d is %A', time.localtime()))
# 相当于用strftime把对应元组的数取出来格式化你想要的效果
# 对应的格式%字母对应元组什么参数可以上网查一下奥

# 3.字符串转时间元组
print(time.strptime('2022-09-29', '%Y-%m-%d'))
# 一个转换而已，注意对应格式相同哦，且只有我们对应了才有值，其他的都是默认值

# 4.时间元组转时间戳

print(time.mktime(time.localtime()))
# mktime(时间元组)
# 返回对应时间戳，当然时间元组我们可以自己定义t=(...)然后mktime(t),也是ok的，但是t必须是9个元素对应那些数


# 一些常用函数
print(time.asctime())  # 参数可有可无是一个时间元组，化成他已经定义好的格式，没有参数默认localtime

print(time.ctime())
# 也是参数可有可无，参数是时间戳，化成asctime()那种格式，没参数，默认用time.time()
