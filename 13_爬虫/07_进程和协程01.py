# 进程就是运行的程序不多讲
# 协程是一种在线程中被调度的函数，也称为微线程，协程的作用：执行函数A随时中断执行函数B,然后等B执行完，再返回来执行A.也可以反过来，类似多线程，不同之处就是协程中只有一个线程在执行
# 优点：1.执行效率高2.没有锁机制3.适用I/O密集型任务

import asyncio      # 协程对应模块
async def func():
    sum01 = 0
    for i in range(10000):
        sum01 = sum01 + i*i*i
#    await asyncio.sleep(1)      # await是用来挂起该协程且执行事件循环的下一个事件的命令，只可用于async对应的函数内
    await fund()        # await后面接可等待对象-有协程对象，Task对象和Future对象,await 后面接协程对象相当于调用对应协程，并调用结束后继续执行此协程
    print(sum01)
async def fund():
    print("333")
    await asyncio.sleep(1)
    print("444")

if __name__ == "__main__":
    result = func()     # 这里的只写这个的话会报错，应为协程你没有执行等待操作，只有主函数运行了,协程函数的调用不会立即执行，而是会返回一个协程对象，协程对象需要注册到事件循环，由事件循环调用；
#    asyncio.run(result)      解决方法1：创建一个事件循环，以result为程序的主入口，执行完毕后关闭事件循环
    loop = asyncio.new_event_loop()     # 解决方法2：用asyncio.get_event_loop()方法创建事件循环，然后用run_until_complete将协程注册到事件循环中
    loop.run_until_complete(result)     # 调用先执行这个协程
    print(result)


