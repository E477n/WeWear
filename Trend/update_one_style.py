def update_one_style(user_id, wid, count):
    import pymongo

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    allcloth = DB.product

    wid = str(wid)
    d = allcloth.find_one({'wid': wid})
    # print(d)

    Cstyle = d['style']

    sty = DB.style
    Estyle = sty.find_one({'Cname': Cstyle})['Ename']

    userstyle = DB.userstyle
    # print(userstyle.find_one({'user_id': user_id}))
    likes = userstyle.find_one({'user_id': user_id})[Estyle]
    likes = likes + count

    userstyle.update({'user_id': user_id}, {'$set': {Estyle: likes}})
    # print(userstyle.find_one({'user_id': user_id}))


# update_one_style('5ab4e211a15a170e6812c088', 1000005, 1)