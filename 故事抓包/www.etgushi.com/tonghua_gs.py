import requests
from bs4 import BeautifulSoup
import json

array = []
page = 1
while (page <= 3):
    print ('The count is:', page)
    # url = http + 域名 + 子路径 + 子路径_是每个页面
    url = 'http://' + 'www.etgushi.com/1001/list_12_' + str(page) + '.html'
    print(url)

    html = requests.get(url)
    #设置编码。不然乱码
    html.encoding='gb2312'

    # 获取全部html内容
    soup = BeautifulSoup(html.text, 'html.parser')
    
    # 找到所有的left-top 循环
    for item in soup.find_all('ul',"left-top"):
        # 循环li标签
        for li in item.find_all('li',""):

            # 找到name所在
            nameItem = li.find('a',"title")
            name = nameItem.text
            print(name)

            #找到详情的url
            link = 'http://www.etgushi.com' + nameItem.attrs['href']
            # print(link)

            #把新的url再轻轻一遍
            openLink = requests.get(link)
            # 同样设置编码
            openLink.encoding='gb2312'
            # 获取全部html内容
            openLinkSoup = BeautifulSoup(openLink.text, 'html.parser')

            # 获取详情的文字
            content = openLinkSoup.p.text
            # print(content)

            # 创建 一个字典
            dic = {
                'name' : name,
                'link' : link,
                'content' : content
            }
            # 把当前添字典加到数组
            array.append(dic)
            # print(array)

    # 到下一页
    page = page + 1

# 转json
jsObj = json.dumps(array)
fileObject = open('一千零一夜.json', 'w')
fileObject.write(jsObj)
fileObject.close()


print('爬取完成')



