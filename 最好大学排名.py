import requests
import bs4
from bs4 import BeautifulSoup
import xlwt
import random
import time #可计算程序运行时间



#获取网页文本
def get_html_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    r = requests.get(url,headers = headers)
    r.encoding = 'utf-8'
    html_text = r.text
    soup = BeautifulSoup(html_text,'lxml')
    return soup

#获取表头信息
def get_thead(soup):
    for tr in soup.find('thead').children:
        if isinstance(tr,bs4.element.Tag):
            ths = tr('th')
            for i in range(len(ths)-1):
                thead.append(ths[i].string)
    for select in soup.find('thead').children:
        if isinstance(select,bs4.element.Tag):
            options = select('option')
            for i in range(len(options)):
                thead.append(options[i].string)
    thead_lenth = len(thead)
    # print(thead_lenth,thead)
    return thead,thead_lenth

#获取表格信息
def get_tr(soup,ulist):
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            #0-12是根据get_thead函数中thead_lenth来定的
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string,
                        tds[5].string,tds[6].string,tds[7].string,tds[8].string,tds[9].string,
                        tds[10].string,tds[11].string,tds[12].string])
    ulist_lenth = len(ulist)
    return ulist,ulist_lenth

#写入本地excel表格
def write_to_excel(ulist,ulist_lenth,year):
    file = xlwt.Workbook()
    sheet = file.add_sheet(year + '_info',cell_overwrite_ok=True)
    sheet.write(0,0,'中国最好大学排名'+ year)
    for i in range(13):
        sheet.write(1,i,thead[i])
    for m in range(ulist_lenth):
        for n in range(13):
                sheet.write(m + 2,n,ulist[m][n])
    file.save(year + '年最好大学排名.xls')

#主函数
if __name__ == '__main__':
    # start = time.clock()
    years = ['2016','2017','2018']
    for year in years:
        thead = []
        ulist = []
        url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming'+ year + '.html'
        soup = get_html_text(url)
        thead,thead_lenth = get_thead(soup)
        ulist,ulist_lenth = get_tr(soup,ulist)
        write_to_excel(ulist,ulist_lenth,year)
        time.sleep(random.randint(0,9))
    # end = time.clock()
    # print(end - start)





























