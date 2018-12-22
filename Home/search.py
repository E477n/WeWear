def search(userid):
    import pymongo

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    c = DB.userstyle

    if c.find_one({"user_id": userid}):
            print('the account already exists.')
    else:
        data = {
                'user_id': userid,
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
        c.insert(data)
        # print('insert successfully!')

# search('5ab3bdbda15a17230cebe044')