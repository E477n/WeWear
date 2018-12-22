def usersty(user_id, style):
    import pymongo
    from . import getPreference

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    styleRule = DB.styleRules

    styleRules = list()
    for each in styleRule.find({"condition": style}):
        styleRules.append([each['action'], each['weight']])

    arr = getPreference.prefer(user_id)
    maxdegree = max(arr[i] for i in arr)
    if maxdegree == 0:
        maxdegree = 1

    for each in styleRules:
        if each[0] == '百搭':
            each[1] = each[1] * (1+arr['allmatch']/maxdegree)
        elif each[0] == '文艺':
            each[1] = each[1] * (1+arr['artistic']/maxdegree)
        elif each[0] == '巴洛克':
            each[1] = each[1] * (1+arr['baroque']/maxdegree)
        elif each[0] == '波西米亚':
            each[1] = each[1] * (1+arr['bohemia']/maxdegree)
        elif each[0] == '英伦':
            each[1] = each[1] * (1+arr['british']/maxdegree)
        elif each[0] == '休闲':
            each[1] = each[1] * (1+arr['casual']/maxdegree)
        elif each[0] == '优雅':
            each[1] = each[1] * (1+arr['elegant']/maxdegree)
        elif each[0] == '民族':
            each[1] = each[1] * (1+arr['folk']/maxdegree)
        elif each[0] == '淑女':
            each[1] = each[1] * (1+arr['gentlewomanly']/maxdegree)
        elif each[0] == '哥特':
            each[1] = each[1] * (1+arr['gothic']/maxdegree)
        elif each[0] == '原宿':
            each[1] = each[1] * (1+arr['harajuku']/maxdegree)
        elif each[0] == '嬉皮':
            each[1] = each[1] * (1+arr['hippie']/maxdegree)
        elif each[0] == '嘻哈':
            each[1] = each[1] * (1+arr['hippop']/maxdegree)
        elif each[0] == '日系':
            each[1] = each[1] * (1+arr['japanese']/maxdegree)
        elif each[0] == '韩版':
            each[1] = each[1] * (1+arr['korean']/maxdegree)
        elif each[0] == '洛丽塔':
            each[1] = each[1] * (1+arr['lolita']/maxdegree)
        elif each[0] == '中性':
            each[1] = each[1] * (1+arr['neutral']/maxdegree)
        elif each[0] == '职业':
            each[1] = each[1] * (1+arr['office']/maxdegree)
        elif each[0] == '学院':
            each[1] = each[1] * (1+arr['preppy']/maxdegree)
        elif each[0] == '朋克':
            each[1] = each[1] * (1+arr['punk']/maxdegree)
        elif each[0] == '运动':
            each[1] = each[1] * (1+arr['sporty']/maxdegree)
        elif each[0] == '街头':
            each[1] = each[1] * (1+arr['street']/maxdegree)
        elif each[0] == '甜美':
            each[1] = each[1] * (1+arr['sweet']/maxdegree)
        elif each[0] == '复古':
            each[1] = each[1] * (1+arr['vintage']/maxdegree)
        elif each[0] == '欧美':
            each[1] = each[1] * (1+arr['western']/maxdegree)
        elif each[0] == '通勤':
            each[1] = each[1] * (1+arr['workday']/maxdegree)

    arr = sorted(styleRules,key = lambda styleRules: styleRules[1], reverse=True)
    # print(arr)
    return arr


# print(usersty('5ab0b251936aa2283c43783c', '通勤'))

