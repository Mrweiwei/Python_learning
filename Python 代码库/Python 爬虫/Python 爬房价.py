import requests
# 用于解析html数据的框架
from bs4 import BeautifulSoup
# 用于操作excel的框架
from xlwt import *
import json
 
# 创建一个工作
book = Workbook(encoding='utf-8');
# 向表格中增加一个sheet表，sheet1为表格名称 允许单元格覆盖
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
# 设置样式
style = XFStyle();
pattern = Pattern();
pattern.pattern = Pattern.SOLID_PATTERN;
pattern.pattern_fore_colour="0x00";
style.pattern = pattern;
# 设置列标题
sheet.write(0, 0, "标题")
sheet.write(0, 1, "地址")
sheet.write(0, 2, "价格")
sheet.write(0, 3, "建筑年代")
sheet.write(0, 4, "满年限")
sheet.write(0, 5, "离地铁")
 
# 设置列宽度
sheet.col(0).width = 0x0d00 + 200*50
sheet.col(1).width = 0x0d00 + 20*50
sheet.col(2).width = 0x0d00 + 10*50
sheet.col(3).width = 0x0d00 + 120*50
sheet.col(4).width = 0x0d00 + 1*50
sheet.col(5).width = 0x0d00 + 50*50
 
# 指定爬虫所需的上海各个区域名称
citys = ['pudong', 'minhang', 'baoshan', 'xuhui', 'putuo', 'yangpu', 'changning', 'songjiang',
         'jiading', 'huangpu', 'jinan', 'zhabei', 'hongkou', 'qingpu', 'fengxian', 'jinshan', 'chongming',
         'shanghaizhoubian']
 
def getHtml(city):
    url = 'http://sh.lianjia.com/ershoufang/%s/' % city
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request = requests.get(url=url, headers=headers)
    # 获取源码内容比request.text好，对编码方式优化好
    respons = request.content
    # 使用bs4模块，对响应的链接源代码进行html解析，后面是python内嵌的解释器，也可以安装使用lxml解析器
    soup = BeautifulSoup(respons, 'html.parser')
    # 获取类名为c-pagination的div标签，是一个列表
    pageDiv = soup.select('div .page-box')[0]
    pageData =dict(pageDiv.contents[0].attrs)['page-data'];
    pageDataObj =json.loads(pageData);
    totalPage =pageDataObj['totalPage']
    curPage =pageDataObj['curPage'];
    print(pageData);
    # 如果标签a标签数大于1，说明多页，取出最后的一个页码，也就是总页数
    for i in range(totalPage):
        pageIndex=i+1;
        print(city+"=========================================第 " + str(pageIndex) + " 页")
        print("\n")
        saveData(city, url, pageIndex);
 
# 调用方法解析每页数据，并且保存到表格中
def saveData(city, url, pageIndex):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    urlStr ='%spg%s' % (url, pageIndex);
    print(urlStr);
    html = requests.get(urlStr, headers=headers).content;
    soup = BeautifulSoup(html, 'lxml')
    liList = soup.findAll("li", {"class": "clear LOGCLICKDATA"})
    print(len(liList));
    index=0;
    for info in liList:
        title =info.find("div",class_="title").find("a").text;
        address =info.find("div",class_="address").find("a").text
        flood = info.find("div", class_="flood").text
        subway = info.find("div", class_="tag").findAll("span", {"class", "subway"});
        subway_col="";
        if len(subway) > 0:
            subway_col = subway[0].text;
 
        taxfree = info.find("div", class_="tag").findAll("span", {"class", "taxfree"});
        taxfree_col="";
        if len(taxfree) > 0:
            taxfree_col = taxfree[0].text;
            
        priceInfo =info.find("div",class_="priceInfo").find("div",class_="totalPrice").text;
        print(flood);
        global row
        sheet.write(row, 0, title)
        sheet.write(row, 1, address)
        sheet.write(row, 2, priceInfo)
        sheet.write(row, 3, flood)
        sheet.write(row, 4,taxfree_col)
        sheet.write(row, 5,subway_col)
        row+=1;
        index=row;
 
# 判断当前运行的脚本是否是该脚本，如果是则执行
# 如果有文件xxx继承该文件或导入该文件，那么运行xxx脚本的时候，这段代码将不会执行
if __name__ == '__main__':
    # getHtml('jinshan')
    row=1
    for i in citys:
        getHtml(i)
    # 最后执行完了保存表格，参数为要保存的路径和文件名，如果不写路径则默然当前路径
    book.save('lianjia-shanghai.xls')
