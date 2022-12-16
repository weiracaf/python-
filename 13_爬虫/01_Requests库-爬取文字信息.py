# Requests 是通过py语言编写的，是用于访问网络资源的第三方库，可以爬取HTML网页界面，模拟人类访问服务器，自动提交网络申请
import requests
import re
# 在来讲请求-get请求-get(url,header)
res = requests.get('http://httpbin.org/get')
# print(res.text)     # 爬取到该网页的信息返回
# header是一个字典类型
url = 'https://movie.douban.com/top250'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0Safari/537.36"
}
# resp = requests.get(url)
# print(resp.text)    # 这里没有把我们想要的结果输出,因为一般网站自带反爬机制，在第二个参数写上对应headers才可以爬，headers可以在网站的network找，最下方的user-agent
resp = requests.get(url, headers=headers)
page_content = resp.text    # 对应单取操作
obj = re.compile(r'</div>.*?<div class="info">.*?<span class="title">(?P<name>.*?)'     # .*?非贪婪匹配（不匹配最长的，一节一个电影名呗）
                 r'</span>.*?<br>(?P<year>.*?)'     # 这里后面没哟.*?应为年份后面紧接着就是&nbsp，可以发现一般的组就是由一个开头+一个结尾来确定组的位置
                 r'&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'   
                 # 只要中间有别的字符串统统用.*?代替，1可以代替别的字符2.非贪婪匹配可以匹配到最近的 
                 r'<span>(?P<num>.*?)</span>', re.S)
# 对应的代码复习re库,主要是？P<变量>不一样，我认为是给每个组赋一个变量名吧
# result = obj.finditer(page_content)
# for it in result:
#    print(it.group("name"))
#    print(it.group("year").strip())
#    print(it.group("score"))
#    print(it.group("num"))
result = obj.findall(page_content)
f = open(r'电影信息.txt', 'w', encoding='utf-8')    # 与文件读写的结合
list01 = []
for i in result:
    list01.append(i[0]+'-'+i[1]+'-'+i[2]+'-'+i[3])
    list01.append('\n')
f.writelines(list01)
f.close()

# 我的理解是，从那么多自分钟搜索对应格式，取出对应字符，结果返回一个元组然后输出
# print(resp.text)    # 会输出对应的前端（html+css+js）语言，输出的是对应界面的源代码
# 但是这里我们把所有的信息都爬取了，如果我们只想爬取对应之中一个电影的信息该怎么办呢？这里我们就要用到re库了




