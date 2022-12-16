import requests
import re


def get_message(num):  # 该方法爬取text
    url = 'https://movie.douban.com/top250?start=' + num + '&filter='
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.0.0 Safari/537.36 "
    }
    resq = requests.get(url, headers=headers)
    page_content = resq.text
    return page_content


def get_picture_url(massage):  # 该方法爬取对应的图片且第一个组是电影名第二个是图片地址
    rest = re.findall(r'<img width="100" alt="(.*?)" src="(.*?)" class="">', massage)
    return rest


def download_picture(picture_url):  # 保存到本地
    for i in picture_url:
        img = requests.get(i[1])
        file = r'D:\学习\图片' + '\\' + i[0] + '.jpg'  # 文件路径+文件名+.jpg（文件后缀）
        with open(file, 'wb') as f:
            f.write(img.content)


if __name__ == "__main__":
    for i in range(0, 100, 25):
        massage = get_message(str(i))
        url_name_list = get_picture_url(massage)
        download_picture(url_name_list)
