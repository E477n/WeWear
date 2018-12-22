import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
DB = connection.mydb
'''
test = DB.category

data1 = {
    'id': '2001',
    'C-Cate2': 'Suit',
    'E_cate2': '套装'
}

data = {
    'id1': '1007',
    'C_cate1': 'Suit',
    'E_cate2': '套装',
    'category2': data1
}

test.insert(data)
'''

test = DB.sex

data = {
    'id': 'S003',
    'Cname': '中',
    'Ename': 'Neutral',
    'description': '中性风服饰是指男、女均适合穿的服饰'
}

test.insert(data)