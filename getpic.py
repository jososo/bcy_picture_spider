import requests
from bs4 import BeautifulSoup
import os
import sys
import re


global dir_path
dir_path = "d:\\bcy.net\\"

def get_page(url):
    response = requests.get(url)
    content = BeautifulSoup(response.text, "html.parser")
    if content.find(text="尾页"):
        return re.sub('(.+p=)|([^0-9]*)', "", str(content.find(text="尾页").parent))
    else:
        return 0


def get_url(url):         #获取网址
    response = requests.get(url)
    content = BeautifulSoup(response.text, "html.parser")

    '''
    global page_tag
    if page_tag == 0:
        page_tag = True
        # 正则表达式匹配尾页数，content.find().parent 表示内容对应的那一个tag
        global page
        if content.find(text="尾页"):
            page = re.sub('(.+p=)|([^0-9]*)', "", str(content.find(text="尾页").parent))
    '''

    url_back = content.find_all(attrs={"class": "db posr ovf"}) #根据HTML修改类型
    url_list = []
    for a in url_back:
        url_list.append(a.attrs.get("href"))
    return url_list


def get_picture(url):         #获取图片
    #作品编号
    item_id = re.search('[0-9]+', url).group(0)
    #粉丝可见标记
    fans_tag = False
    #作品地址
    url = "https://bcy.net"+url
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    # 作者名称
    name = content.find(class_='user-name').get_text()
    html_script = content.find_all('script')
    aim_script = ''
    for i in html_script:
        if 'window.__ssr_data' in i.text:
            aim_script = i
            break

    url_list = []
    aim_script = aim_script.text.split(",")
    for i in aim_script:

        if 'original_path' in i:
            i = re.sub(r".*https", "", i)
            i = re.sub(r"\\\\u002F", "/", i)
            i = "https"+re.sub(r"\\\"}||]", "", i)
            url_list.append(i)
        elif'粉丝可见' in i:
            fans_tag = True
            break

    if not(url_list or fans_tag):
        return None

    path = dir_path+name+'_'+item_id
    if not os.path.exists(path):
        # 如果不存在则创建目录
        os.makedirs(path)
        print(name+'_'+item_id + " 作品开始保存")
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(name+'_'+item_id+" 已保存作品，无需重复保存")
        print("_________________________________")
        return None

    if fans_tag:
        fp = open(path+'/粉丝可见.txt ', 'w')
        fp.close()
    else:
        j = 1
        for i in url_list:
            fp = open(path + '/' + str(j) + '.jpg ', 'wb+')
            fp.write(requests.get(i, timeout=30).content)
            fp.close()
            j += 1

    print("保存完成")
    print("_________________________________")


if __name__ == '__main__':
    print("输入你要搜索的关键字吧，就跟半次元里的搜索一样（默认路径D：\ bcy.net 保存图片）")
    name = input()
    print("如果想更改图片保存路径请以类似D：\ bcy.net 的格式输入路径，否则请输入回车（Enter）")
    path = input()
    if path != "":
        print("保存路径修改为："+path)
        dir_path = path

    dir_path = dir_path+name+'\\'
    url = "https://bcy.net/search/home?k="+name
    page = int(get_page(url))

    if page == 0:
        print("无相关内容")
        sys.exit(1)

    for i in range(1, page+1):
        print(i)
        print("_________________________________")
        u_l = get_url(url + "&p="+str(i))
        for i in u_l:
            try:
                get_picture(i)
            except:
                continue
