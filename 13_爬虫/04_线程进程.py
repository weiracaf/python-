#  程序：静态的代码
#  进程：动态的，是一个程序的执行过程，是执行中的程序
#  线程：比进程小的执行单位，进程可以产生多个线程
import threading  # 线程对应模块
import time


# 多线程-1.创建线程对象2.启动线程执行任务
# 线程类Thread包含target！是执行目标的任务名 ， args，kwargs元组/字典方式给任务传参 dameon是否守护线程的属性
def sing(num, name):
    for i in range(num):
        print(name)
        time.sleep(0.5)
def dance(count):
    for i in range(count):
        print("跳舞")
        time.sleep(0.6)
if __name__ == "__main__":
    t1 = threading.Thread(target=sing, args=(3, "小袁"))    # 创建线程对象  注意只写函数名称不加括号（所以要用别的方式传参）,元组传参注意是传到对应的target对应的函数
    t2 = threading.Thread(target=dance, kwargs={"count": 3})    # 以字典方式传参,关键字要对应
    t1.start()
    t2.start()

