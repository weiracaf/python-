
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
    t2 = threading.Thread(target=dance, daemon=True)    # daemon默认False主线程想结束等为False的子线程执行完，设置为True就子线程不管直接结束对应内部子线程也结束
    time_start = time.time()
    t1.start()
    t2.start()
# 正常主线程会等子线程执行完毕后再结束，可以通过设置daemon来解决
# 在脚本运行过程中有一个主线程，若在主线程中创建了子线程，当主线程结束时根据子线程daemon属性值的不同可能会发生下面的两种情况之一：

# 如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；

# 如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。

