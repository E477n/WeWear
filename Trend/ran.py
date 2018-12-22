def randomNewProduct():
    import pymongo
    import random

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    allcloth = DB.product

    arr = list()
    for each in allcloth.find({'release_time': {'$regex': '2018'}}):
        arr.append(each['wid'])

    random.shuffle(arr)
    return arr
print(randomNewProduct())