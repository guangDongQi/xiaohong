# 使用 requests 做网络请求
#     lxml 解析数据 这个也是比较主流的
#     xpath 语法 寻找节点


import requests
from lxml import etree
import json

array = []

# 获取主页面输入

url = "https://gushi.1or9.com/gushifenlei.html"

response = requests.get(url=url)

response.encoding = response.apparent_encoding

html = etree.HTML(response.text)

links = html.xpath('/html/body/div[2]/main/div/div/article/div/div/h2/a/@href')

# 获取主页面下子分类

for link in links:

    listLink = 'https://gushi.1or9.com' + link

    listResponse = requests.get(url=listLink)

    listResponse.encoding = response.apparent_encoding

    listHtml = etree.HTML(listResponse.text)

    page = 1
    totalPage = 1
    lu_list = listHtml.xpath('/html/body/div[2]/main/div/div/nav/ul/li')
    title_name = listHtml.xpath('/html/body/div[2]/main/div/div/section[1]/h1/text()')[0]
    if len(lu_list) >= 15:
        right_text_xpath = '/html/body/div[2]/main/div/div/nav/ul/li[15]/a/text()'
        right_text = listHtml.xpath(right_text_xpath)[0]
        pageLiHref = listHtml.xpath('/html/body/div[2]/main/div/div/nav/ul/li[15]/a/@href')[0]
        pageLiHref = pageLiHref.replace(link + '/page', '')
        pageLiHref = pageLiHref.replace('/', '')

        print('有多页，共：' + pageLiHref)
        totalPage = int(pageLiHref)
    else:
        
        totalPage = len(lu_list)
        print('共有' + str(totalPage) + '页')

    

    while (page <= totalPage):

        pageLink = ''
        pageHtml = ''
        if page == 1:

            pageLink = 'https://gushi.1or9.com' + link
            listResponse = requests.get(url=pageLink)
            listResponse.encoding = response.apparent_encoding
            pageHtml = etree.HTML(listResponse.text)

        else:

            pageLink = 'https://gushi.1or9.com' + link + '/page/' + str(page)
            listResponse = requests.get(url=pageLink)
            listResponse.encoding = response.apparent_encoding
            pageHtml = etree.HTML(listResponse.text)

        # 爬取故事列表
        
        list_div = pageHtml.xpath('/html/body/div[2]/main/div/div/section[2]/article')
        count = 1
        while (count <= len(list_div)):
            
            # 故事内容url
            content_url = pageHtml.xpath('/html/body/div[2]/main/div/div/section[2]/article/header/h2/a/@href')

            url = content_url[count - 1]

            content_Link = 'https://gushi.1or9.com' + url

            content_Response = requests.get(url=content_Link)

            content_Response.encoding = response.apparent_encoding

            content_Html = etree.HTML(content_Response.text)
        
            name = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/h1/text()')

            tag = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/div/a/text()')

            time = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/time/text()')[0]
            time = time.replace('\n', '')
            time = time.replace(' ', '')

            text_count = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/span[1]/text()')

            redCount = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/span[2]/text()')
            
            content = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/div[1]/p/text()')

            dic = {
                    'name' : name[0],
                    'link' : content_Link,
                    'content' : content,
                    'tag':tag[0],
                    'time':time,
                    'textCount':text_count[0],
                    'redCount':redCount[0],
                }

            print(dic)

            array.append(dic)

            print('爬取-' + name[0])

            count = count + 1

            

        print(str(page) + '页爬取完毕' + '共计:' + str(len(array)) + '故事')


        page = page + 1 

    print(title_name + '爬取完毕' + '共计:' + str(len(array)) + '故事')




# 转json
jsObj = json.dumps(array)
fileObject = open('gushi.1or9.com.json', 'w')
fileObject.write(jsObj)
fileObject.close()


print('爬取完成')

