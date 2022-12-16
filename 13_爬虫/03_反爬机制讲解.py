# 本文主要讲反爬机制，就是上两篇文章的headers
# headers不讲了，就是在开发中工具的network里随便找一个文件划到最下方，有那个User-Agent : 博拉博拉的
# 设置多个代理ip，就是你应该网站，访问多次的话，就无法继续访问这个网站，就无法爬取了
# 主要操作是 代理ip池+随机函数+更改ip操作
# 还有一个随机休眠机制，爬虫的访问时间是固定的，这样会被检测，为了不被检测进行随机休眠，time模块的sleep和random的联动
import random
import time

import requests

proxies_list = [  # 序列
    # 代理ip池
]
for i in range(10):
    random_proxies = random.choice(proxies_list)  # 随机找从代理ip池找一个代理ip
    try:
        proxies = {'http': random_proxies}  # 代理真正的ip，字典类型
    #   r = requests.get(url=(网址),header=,proxies=(代理ip) )  如果所有代理ip被封，报错
    except:  # 进行替换ip的操作
        proxies_list.remove(random_proxies)  # 先删除被封的代理ip
        random_proxie = random.choice(proxies_list)  # 换一个新的ip
        proxies = {'http': random_proxie}
# r = requests.get(url,headers,proxies)
# r.encoding = 'utf-8'
# print(r.text)
time.sleep(random.randint(1, 3))    # 随机休眠
a = 1
# 但是当代理ip的所有都被禁的时候我们也无法爬取
# 我们可以用 try 异常处理机制来做
