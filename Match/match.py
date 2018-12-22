def match(cate2, sex, season, sty, user_id):
    import pymongo
    import math
    from . import userstyle

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    cate2Rule = DB.cate2Rules
    sexRule = DB.sexRules
    seasonRule = DB.seasonRules

    allcloth = DB.product

    sexRules = list()
    seasonRules = list()
    styleRules = list()

    for each in sexRule.find({"condition": sex}).sort("weight", pymongo.DESCENDING):
        sexRules.append(each['action'])
    for each in seasonRule.find({"condition": season}).sort("weight", pymongo.DESCENDING):
        seasonRules.append(each['action'])
    for each in userstyle.usersty(user_id, sty):
        styleRules.append(each[0])
    # print(styleRules)

    # 确定sex， season， style的搭配
    action = list()
    for k in range(0, 5):  # style
        action.append([sexRules[0], seasonRules[0], styleRules[k]])
    # print(action)

    array_main = list()

    # 确定category的搭配
    # 外套层次
    coat = []
    for each in cate2Rule.find({"condition": cate2, "category1": '外套'}).sort("weight", pymongo.DESCENDING):
        coat.append(each['action'])
    # print(coat)
    num1 = math.ceil(0.3*len(coat))
    array1 = []
    if num1 != 0:
        for each in action:
            for i in range(0, num1):
                array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": coat[i]},
                                           {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array1.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array1)
    array_main.append(sorted(array1, key=lambda x:x[1]))

    # 上装层次
    tops = []
    for each in cate2Rule.find({"condition": cate2, "category1": '上装'}).sort("weight", pymongo.DESCENDING):
        tops.append(each['action'])
    # print(tops)
    num2 = math.ceil(0.3 * len(tops))
    array2 = []
    if num2 != 0:
        for each in action:
            for i in range(0, num2):
                array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": tops[i]},
                                           {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array2.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array2)
    array_main.append(sorted(array2, key=lambda x:x[1]))

    # 内衬层次
    lining = []
    for each in cate2Rule.find({"condition": cate2, "category1": '内衬'}).sort("weight", pymongo.DESCENDING):
        lining.append(each['action'])
    # print(lining)
    num3 = math.ceil(0.3 * len(lining))
    array3 = []
    if num3 != 0:
        for each in action:
            for i in range(0, num3):
                array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": lining[i]},
                                            {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array3.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array3)
    array_main.append(sorted(array3, key=lambda x:x[1]))

    # 内搭层次
    inside = []
    for each in cate2Rule.find({"condition": cate2, "category1": '内搭'}).sort("weight", pymongo.DESCENDING):
        inside.append(each['action'])
    # print(inside)
    num4 = math.ceil(0.3 * len(inside))
    array4 = []
    if num4 != 0:
        for each in action:
            for i in range(0, num4):
                array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": inside[i]},
                                            {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array4.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array4)
    array_main.append(sorted(array4, key=lambda x:x[1]))

    # 连体套装层次
    piece_suit = []
    for each in cate2Rule.find({"condition": cate2, "category1": '连体套装'}).sort("weight", pymongo.DESCENDING):
        piece_suit.append(each['action'])
    # print(piece_suit)
    num5 = math.ceil(0.3 * len(piece_suit))
    array5 = []
    if num5 != 0:
        for each in action:
            for i in range(0, num5):
                array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": piece_suit[i]},
                                            {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array5.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array5)
    array_main.append(sorted(array5, key=lambda x:x[1]))

    # 连衣套装层次
    dress_suit = []
    for each in cate2Rule.find({"condition": cate2, "category1": '连衣套装'}).sort("weight", pymongo.DESCENDING):
        dress_suit.append(each['action'])
    # print(dress_suit)
    num6 = math.ceil(0.3 * len(dress_suit))
    array6 = []
    if num6 != 0:
        for each in action:
            for i in range(0, num6):
                array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": dress_suit[i]},
                                            {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array6.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array6)
    array_main.append(sorted(array6, key=lambda x:x[1]))

    # 西装套装层次
    suit = []
    for each in cate2Rule.find({"condition": cate2, "category1": '西装套装'}).sort("weight", pymongo.DESCENDING):
        suit.append(each['action'])
    # print(suit)
    num7 = math.ceil(0.3 * len(suit))
    array7 = []
    if num7 != 0:
        for each in action:
            for i in range(0, num7):
                array = list(
                    allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": suit[i]},
                                  {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array7.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array7)
    array_main.append(sorted(array7, key=lambda x:x[1]))

    # 裤装层次
    trousers = []
    for each in cate2Rule.find({"condition": cate2, "category1": '裤装'}).sort("weight", pymongo.DESCENDING):
        trousers.append(each['action'])
    # print(trousers)
    num8 = math.ceil(0.3 * len(trousers))
    array8 = []
    if num8 != 0:
        for each in action:
            for i in range(0, num8):
                array = list(
                    allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": trousers[i]},
                                  {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array8.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array8)
    array_main.append(sorted(array8, key=lambda x:x[1]))

    # 裙装层次
    skirt = []
    for each in cate2Rule.find({"condition": cate2, "category1": '裙装'}).sort("weight", pymongo.DESCENDING):
        skirt.append(each['action'])
    # print(skirt)
    num9 = math.ceil(0.3 * len(skirt))
    array9 = []
    if num9 != 0:
        for each in action:
            for i in range(0, num9):
                array = list(
                    allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": skirt[i]},
                                  {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array9.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array9)
    array_main.append(sorted(array9, key=lambda x:x[1]))

    # 鞋子层次
    shoes = []
    for each in cate2Rule.find({"condition": cate2, "category1": '鞋子'}).sort("weight", pymongo.DESCENDING):
        shoes.append(each['action'])
    # print(shoes)
    num10 = math.ceil(0.3 * len(shoes))
    array10 = []
    if num10 != 0:
        for each in action:
            for i in range(0, num10):
                array = list(
                    allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": shoes[i]},
                                  {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array10.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array10)
    array_main.append(sorted(array10, key=lambda x:x[1]))

    # 配饰层次
    accessories = []
    for each in cate2Rule.find({"condition": cate2, "category1": '配饰'}).sort("weight", pymongo.DESCENDING):
        accessories.append(each['action'])
    # print(accessories)
    num11 = math.ceil(0.3 * len(accessories))
    array11 = []
    if num11 != 0:
        for each in action:
            for i in range(0, num11):
                array = list(
                    allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": accessories[i]},
                                  {"wid": 1, "_id": 0, "colorhsl": 1, "price": 1}))
                for j in array:
                    array11.append([j['wid'], float(j['colorhsl'][0]), float(j['colorhsl'][1]), float(j['colorhsl'][2]), j['price']])
    # print(array11)
    array_main.append(sorted(array11, key=lambda x:x[1]))

    return array_main


# print(match('连帽卫衣', '女', '春', '通勤', '5ab0b251936aa2283c43783c'))