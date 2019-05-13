'''
    https://tieba.baidu.com/f?kw=%E7%A9%BA%E6%B4%9E%E9%AA%91%E5%A3%AB&pn=0
    https://tieba.baidu.com/f?kw=%E7%A9%BA%E6%B4%9E%E9%AA%91%E5%A3%AB&pn=50
    https://tieba.baidu.com/f?kw=%E7%A9%BA%E6%B4%9E%E9%AA%91%E5%A3%AB&pn=100
    https://tieba.baidu.com/f?kw=%E7%A9%BA%E6%B4%9E%E9%AA%91%E5%A3%AB&pn=150

'''
from urllib import request,parse


def tiebaSpider(url,beginPage,endPage):
    '''
    作用：处理url，分配每一个url发送请求
    :param url: 需要请求的资源地址
    :param beginPage: 需要爬取的起始页面
    :param endPage: 需要爬取的结束页面
    '''
    for page in range(beginPage,endPage+1):
        fileName = "第"+str(page) +"页.html"
        # 0 * 50 第一页   1 *50 第二页  2*50 第三页 ......
        pn= (page-1) * 50
        # 得到每一页的url地址
        page_url = url +"&pn="+str(pn)
        print(page_url)
        # 通过每一页的url地址取向服务器发起请求（加载一个页面）
        data = loadPage(page_url, fileName)
        # 将每一个页面写入硬盘中
        writeFile(data,fileName)
        print("-------------------------------下载完成！--------------------------------------------")

def loadPage(page_url,fileName):
    '''
    作用：根据每一个url，向服务器发起请求
    :param page_url: 每一页的url地址
    :param fileName: 文件名
    :return: 每一页的源代码
    '''
    print("正在下载"+ fileName)
    ua_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    req = request.Request(page_url,headers=ua_header)
    data = request.urlopen(req).read().decode()
    return  data


def writeFile(data,fileName):
    '''
    作用：将每一页的源代码，保存到硬盘中，就需要用到文件的写入（open()）
    :param data: 每一页的源代码
    :param fileName: 文件名
    '''
    file = open(fileName,"w",encoding="utf-8")
    file.write(data)
    file.close()



kw = input("请输入您要爬取的贴吧名称：")
beginPage = input("爬取的起始页：")
endPage = input("爬取的结束页：")
# 将str转int
beginPage = int(beginPage)
endPage = int(endPage)
# 需要爬去贴吧的url地址
url = "https://tieba.baidu.com/f?kw="
# url编码
kw = parse.quote(kw)
#  这个地址只拼接了需要爬取的贴吧名称，没有指定爬哪一页
new_url = url + kw
#print(new_url)

# 调用 tiebaSpider 函数
tiebaSpider(new_url,beginPage,endPage)



