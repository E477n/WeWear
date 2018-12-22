def main_match(info):
    import json
    from django.http import HttpResponse
    import requests
    from bs4 import BeautifulSoup
    import urllib
    from . import style
    import re
    from . import getHSL
    from . import match
    from . import color_match
    from . import color_all
    import pymongo
    from . import sex

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    allcloth = DB.product
    case = DB.case

    # 检查url是否能正常打开
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
    try:
        url = info[1]
        # 淘口令
        pattern = re.compile(r'[（|(].*[）|)]')
        m = pattern.search(url)
        if m != None:
            content = m.group()
            title = content.strip()[1:-1]
            print(title)
            url_tkl = 'https://s.taobao.com/search?q=' + title
            resp = requests.get(url_tkl)
            resp.encoding = 'utf-8'
            pics = re.findall(r'"pic_url":"([^"]+)"', resp.text, re.I)
            for each in pics:
                image = 'http:' + each
            print(image)
        else:
            # 从淘宝或天猫上获取衣服title，图片和上市季节
            web_data = requests.get(url)
            # web_data.encoding = "utf-8"
            Soup = BeautifulSoup(web_data.text, 'lxml')
            pics = Soup.select('img#J_ImgBooth')  # 衣服图片
            titles = Soup.select('h3.tb-main-title')  # 衣服标题 淘宝网
            if not titles:  # 天猫
                titles = Soup.select('div.tb-detail-hd > h1')

            # 获得衣服title
            if not titles:
                return '所给url不是所需url地址，无法获取相关信息，请检查后重试！'
            if not pics:
                return '所给url不是所需url地址，无法获取相关信息，请检查后重试！'
            title = titles[0].get_text().strip()
            print(title)
            image = 'http:' + pics[0].get('src').strip()
            print(image)

        # 衣服种类匹配
        cate1 = info[2]
        cate2 = info[3]

        # 性别匹配
        sex1 = '中'
        sex1 = sex.sex_match(title)
        # print("sex:", sex)

        # 季节匹配
        season = '适宜的季节'
        pattern = re.compile('[夏|冬|秋|春]')
        m = pattern.search(title)
        if m != None:
            season = m.group()
        if season == '适宜的季节':
            season = '春'
        print(season)

        # 风格匹配
        sty = '百搭'
        sty = style.style_match(title)
        # print("style:", sty)

        # 颜色识别
        color = list()
        for each in pics:
            image = 'https:' + each.get('src').strip()
        for each in getHSL.HSL(image):
            color.append(float(each))
        if len(color) == 0:
            color = [0, 0, 0]
        # print("color:", color)

        # print('初始搭配')
        matching = list()
        matching = match.match(cate2, sex1, season, sty, info[0])
        # print("matching:", matching)

        # print('色系搭配')
        scheme = list()
        scheme = color_match.color_match(color, matching)
        # for each in scheme:
        #    print("colormatching:", each)

        # print('主题色搭配')
        final = list()
        final = color_all.allcolor(scheme)
        # print("final:", final)

        # 转成dict数据类型
        matchset = {}
        count1 = 1
        for i in final:
            name1 = 'matchset' + str(count1)
            temp = {}
            count2 = 1
            for j in i:
                if j:
                    name2 = 'clothes' + str(count2)
                    temp[name2] = allcloth.find_one({"wid": j}, {'_id': 0, 'wid': 1, 'brand': 1, 'title': 1, 'price': 1, 'url': 1, 'composition': 1})
                count2 += 1
            matchset[name1] = temp
            count1 += 1
        # print("matchset:", matchset)

        # 将用户信息转换成dict形式
        pattern = re.compile('\d{12}')
        m = pattern.search(image)
        if m != None:
            number = m.group()
        else:
            number = '123456789101'
        user_detail = {}
        user_detail['title'] = title
        user_detail['url'] = str(info[0])
        user_detail['image'] = number
        # print(user_detail)

        # 将所有信息打包成dict数据传到前端
        all_info = {}
        all_info['matchset'] = matchset
        all_info['userdetail'] = user_detail
        # print(all_info)

        # 将搭配套装存入数据库
        user_id = info[0]
        cases = [user_id, title, url, cate1, cate2, sex1, season, sty, image, color, final]
        cloth2 = list()
        for i in cases[10]:
            if i:
                for j in i:
                    for each in allcloth.find({"wid": j}):
                        cloth2.append([each['title'], each['url'], each['category1'], each['category2'], each['sex'],
                                      each['season'], each['style'], each['img'], each['colorhsl'], each['wid']])

        for each in cloth2:
            data = {
                'user_id': cases[0],
                '1title': cases[1],
                '1url': cases[2],
                '1category1': cases[3],
                '1category2': cases[4],
                '1sex': cases[5],
                '1season': cases[6],
                '1style': cases[7],
                '1img': cases[8],
                '1color': cases[9],
                '2title': each[0],
                '2url': each[1],
                '2category1': each[2],
                '2category2': each[3],
                '2sex': each[4],
                '2season': each[5],
                '2style': each[6],
                '2img': each[7],
                '2color': each[8],
                '2wid': each[9],
                'likes': 0
            }
            case.insert(data)
        # print('insert successfully!')
        # print(all_info)
        return all_info

    except urllib.error.HTTPError:

        return '所给url不是正确的淘口令或url地址，无法正常访问，请检查后重试1！'

    except urllib.error.URLError:

        return '所给url不是正确的淘口令或url地址，无法正常访问，请检查后重试2！'

    except:

        return '所给url不是正确的淘口令或url地址，无法正常访问，请检查后重试3！'