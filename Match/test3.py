import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
DB = connection.WeWear
allcloth = DB.allcloth

test = {}
name = 'matchset'
test[name]= allcloth.find_one({"wid": '1021580'}, {'_id': 0, 'brand': 1, 'title': 1, 'price': 1, 'url': 1, 'composition': 1, 'descriptions': 1})

print(test)