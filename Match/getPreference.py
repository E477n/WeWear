def prefer(user_id):
    import pymongo

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    pre = DB.userstyle

    if pre.find_one({"user_id": user_id}):
        sty_prefer = pre.find_one({"user_id": user_id}, {'_id': 0, 'user_id': 0})
    else:
        sty_prefer = {
            'allmatch': 0,
            'artistic': 0,
            'baroque': 0,
            'bohemia': 0,
            'british': 0,
            'casual': 0,
            'elegant': 0,
            'folk': 0,
            'gentlewomanly': 0,
            'gothic': 0,
            'harajuku': 0,
            'hippie': 0,
            'hippop': 0,
            'japanese': 0,
            'korean': 0,
            'lolita': 0,
            'neutral': 0,
            'office': 0,
            'preppy': 0,
            'punk': 0,
            'sporty': 0,
            'street': 0,
            'sweet': 0,
            'vintage': 0,
            'western': 0,
            'workday': 0
        }

    # print(sty_prefer)

    return sty_prefer


# prefer('5ab0b2519362283c43783c')




