from mongoengine import *
connect('mydb', host='localhost', port=27017)

class products(Document):

    id = StringField(length=7)
    tid = StringField(length=12)
    pid = StringField(max_length=16)
    brand = StringField(max_length=32)
    title = StringField(max_length=128)
    colorhsl = StringField(max_length=16)
    price = IntField
    sex = StringField(length=1)
    season = StringField(max_length=2)
    style = StringField(max_length=4)
    category1 = StringField(max_length=8)
    category2 = StringField(max_length=8)
    color = StringField(max_length=8)


    meta = {'collection': 'db_clr_pdc'}
#connection test
# products = db_clr_pdc.objects.all()
# for i in products:
#     print("brand:", i.brand, ",number:", i.number, ",color:", i.color)
# print("finish")