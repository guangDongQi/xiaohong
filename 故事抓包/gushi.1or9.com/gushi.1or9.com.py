# 使用 requests 做网络请求
#     lxml 解析数据 这个也是比较主流的
#     xpath 语法 寻找节点


import requests
from lxml import etree

array = []

url = "https://gushi.1or9.com/gushifenlei.html"

response = requests.get(url=url)

response.encoding = response.apparent_encoding

html = etree.HTML(response.text)

links = html.xpath('/html/body/div[2]/main/div/div/article/div/div/h2/a/@href')

for link in links:

    listLink = 'https://gushi.1or9.com' + link

    listResponse = requests.get(url=listLink)

    listResponse.encoding = response.apparent_encoding

    listHtml = etree.HTML(listResponse.text)

    list_div = listHtml.xpath('/html/body/div[2]/main/div/div/section[2]/article')


    page = 1
    totalPage = 1
    right = listHtml.xpath('/html/body/div[2]/main/div/div/nav/ul/li[17]/a/text()')[0]

        if right == '»»':
            pageLiHref = listHtml.xpath('/html/body/div[2]/main/div/div/nav/ul/li[17]/a/text()')[0]
            pageLiHref = pageLiHref.replace(link + '/page', '')
            pageLiHref = pageLiHref.replace('/', '')

            print(pageLiHref);

            totalPage = int(pageLiHref)

    while (page <= totalPage):


    count = 1
    while (count <= len(list_div)):

        content_url = listHtml.xpath('/html/body/div[2]/main/div/div/section[2]/article/header/h2/a/@href')

        url = content_url[count - 1]

        content_Link = 'https://gushi.1or9.com' + url

        content_Response = requests.get(url=content_Link)

        content_Response.encoding = response.apparent_encoding

        content_Html = etree.HTML(content_Response.text)
    
        name = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/h1/text()')

        tag = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/div/a/text()')

        time = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/time/text()')

        text_count = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/span[1]/text()')

        redCount = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/header/div/span[2]/text()')
        
        content = content_Html.xpath('/html/body/div[2]/main/div/div/article[1]/div[1]/text()')

        dic = {
                'name' : name[0],
                'link' : content_Link,
                'content' : content,
                'tag':tag[0],
                'time':time[0],
                'textCount':text_count[0],
                'redCount':redCount[0],
            }

        array.append(dic)

        print('爬取-' + name[0])

        count = count + 1
 


# 转json
jsObj = json.dumps(array)
fileObject = open('一千零一夜.json', 'w')
fileObject.write(jsObj)
fileObject.close()


print('爬取完成')




    


# import requests
# from lxml import etree
# import json

# url = 'https://gushi.1or9.com/gushifenlei.html'
# req = requests.get(url)
# req.encoding = 'utf-8'

# html = etree.HTML(req.text)

# print(html.text)

# # html_data = etree.tostring(html)

# # html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//*')


# name = html.xpath('//*[@id="content"]/article/div/div/h2/text()')

# print(name)


# # print(html.text)

# # 获取全部html内容
# soup = BeautifulSoup(html.text, 'html.parser')


# # print(html.text)

# for item in soup.find_all('div',"post-content"):
    

#     for h2 in item.find_all('h2',''):

#         name = h2.text
#         print(name)

#         link = h2.a.attrs['href']
#         print(link)

#         # 获取page 用
#         itemHtml = requests.get('https://gushi.1or9.com' + link)
#         itemHtml.encoding='utf-8'
#         itemSoup = BeautifulSoup(itemHtml.text, 'html.parser')

#         # 获取总页数
#         for pageItem in itemSoup.find_all('nav',"pagination"):

#             # print(pageItem)
#             page = 1
#             totalPage = 1
#             for pageLi in pageItem.find_all('li',''):

#                 if pageLi.text == '»»':
#                     pageLiHref = pageLi.a['href']
#                     pageLiHref = pageLiHref.replace(link + '/page', '')
#                     pageLiHref = pageLiHref.replace('/', '')

#                     print(pageLiHref);

#                     totalPage = int(pageLiHref)

#             while (page <= totalPage):

#                 pageList = 'https://gushi.1or9.com' + link
#                 if page != 1 :
#                     pageList = 'https://gushi.1or9.com' + link + '/page/' + str(page)

#                 pageListHtml = requests.get(pageList)
#                 pageListHtml.encoding='utf-8'
#                 pageItemSoup = BeautifulSoup(pageListHtml.text, 'html.parser')

#                 print(pageListHtml.text)

#                 for pageItemInfo in pageItemSoup.find_all('div',"mobile-panel"):

#                     print(pageItemInfo)

#                     break

#                 break

#             break

#         break    

#     break