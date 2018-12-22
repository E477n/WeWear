import requests
from bs4 import BeautifulSoup


def Title(url):
    # 从淘宝或天猫上获取衣服title，图片和上市季节
    # url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.90.6d8e6359lRrrHZ&id=543836899086&ns=1&abbucket=19'
    web_data = requests.get(url)
    # web_data.encoding = "utf-8"
    Soup = BeautifulSoup(web_data.text, 'lxml')
    pics = Soup.select('img#J_ImgBooth')   #衣服图片
    titles = Soup.select('h3.tb-main-title')   #衣服标题
    lis = Soup.select('ul.attributes-list > li')  #衣服季节
    if not titles:
        titles = Soup.select('div.tb-detail-hd > h1')
        lis = Soup.select('ul#J_AttrUL > li')
    seasons = list()
    for each in lis:
        seasons.append(each.get_text().strip())

    title = '待搭配服饰'
    for each in titles:
        title = each.get_text().strip()

    return title