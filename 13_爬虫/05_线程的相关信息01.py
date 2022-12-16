# 1.线程的执行顺序是无序的,唱歌跳舞共同执行，看谁先抢到GTL锁开门
import threading
import time
def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(0.5)
def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(0.6)
if __name__ == "__main__":
    t1 = threading.Thread(target=sing, daemon=True)
    t2 = threading.Thread(target=dance, daemon=True)
    time_start = time.time()
    t1.start()
    t2.start()
    t1.join()   # 该方法会将主线程阻塞在该行代码
    t2.join()   # 该方法将主线程阻塞，调用的线程执行完毕
    print(threading.enumerate())    # 获取当前运行的线程的名称和数量,对应输出三个线程-main_thread,thread1和thread2
    time_end = time.time()
    print(time_end-time_start)  # 可以看出我们想得到运行程序的时间，但是你会发现，子线程还没执行完这行代码就会执行，不符合我们的预期，怎么使子线程结束后再进行主线程呢，可以用join()函数





# 当然也可以规定执行顺序用threading.Lock()
# CPU密集型任务（计算密集型任务）使用多线程反而比不使用多线程耗时多，因为GTL锁
# 比如下面这个就是CPU密集型任务
def shu():
    sum1 = 0
    for i in range(10000):
        sum1 = sum1 + i*i
def shu2():
    sum2 = 0
    for i in range(10000):
        sum2 = sum2 + i*i*i

