import asyncio
import time
# 我们发现奥，其实这样的07写的协程都是等那个对应的别的协程运行完才执行循环事件的下一个协程
# 当我们函数有await asyncio.sleep(1)，能不能让在这个等待的时间里去执行下一个进程
# 等这个等待结束，再回来执行呢？，可以-Task对象
# task特性-执行有等待的话会直接进入下一个循环事件
async def func():
    print("111")
    await asyncio.sleep(2)
    print("222")
    return 0
async def fund():
    print("333")
    await asyncio.sleep(2)
    print("444")
    return 1
# 获取协程返回值，把task对象放在列表(task_list=[task1 , task2]) 然后 done ,pending = await asyncio.wait(task_list),
# wait方法返回两个对象有关done是一个set集合是已完成的task对象返回值。pending超时未完成的task对象，用ret.result()获取每个task对象的的返回值
async def main():
    # 创建task将func和fund加入事件循环
    # 但是不会执行，因为此时的main还没执行完
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(fund())
    # 当执行某处协程遇到阻塞-await sleep那个的时候，会自动切换到事件循环的其他任务
    await task1     # 比如task1遇到阻塞，await asyncio.sleep(1)会回来main函数向下走
    print("我task2还没让等")
    await task2     # 然后又遇到这个就执行这个呗,还是等func()的sleep完回去，task1执行完又是主程序，又task2，又main结束
if __name__ == "__main__":
    asyncio.run(main())


