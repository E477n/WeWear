from django.db import models
from mongoengine import *
from . updatesty import update_sty
connect('mydb', host='localhost', port=27017)

# Create your models here.
class product(Document):
    _id = ObjectIdField()
    tid = StringField(length=12)
    pid = StringField(max_length=16)
    brand = StringField(max_length=32)
    title = StringField(max_length=128)
    colorhsl = StringField(max_length=16)
    price = StringField()
    sex = StringField(length=1)
    season = StringField(max_length=2)
    style = StringField(max_length=4)
    category1 = StringField(max_length=8)
    category2 = StringField(max_length=8)
    color = StringField(max_length=8)
    img = StringField()
    url = StringField()
    composition = StringField()
    descriptions = StringField()
    element = StringField(max_length=16)
    pattern = StringField(max_length=16)
    sleeve_length = StringField(max_length=16)
    shape = StringField(max_length=16)
    sleeve_type = StringField(max_length=16)
    collar_type = StringField(max_length=16)
    fly = StringField(max_length=16)
    length = StringField(max_length=16)
    waist = StringField(max_length=16)
    LEG = StringField(max_length=16)
    size = StringField(max_length=64)
    search_time = StringField()
    tag = StringField(max_length=64)
    release_time = StringField(max_length=16)
    favour_count = StringField(max_length=16)
    wid = StringField(length=7)

    meta = {'collection': 'product'}

    def updateFavour_count(idvalue, value):
        product.objects(wid=idvalue).update_one(favour_count=value)
        # print("view:"+ product.objects(wid=idvalue)[0].favour_count)
        return product.objects(wid=idvalue)[0].favour_count

    def getStyleById(pdc_id):
        pdc_style = product.objects(wid=pdc_id)[0].style
        return pdc_style
#connection test
# product = products.objects.all()
# for i in product[8000:8010]:
#     print("brand:", i.brand, ",id:", i.id, ",title:", i.title)
# print("finish")

class user(Document):
    _id = StringField()
    username = StringField(max_length=16)
    password = StringField(max_length=16)
    email = EmailField(max_length=16)
    sex = StringField(length=1)
    birthday = DateTimeField(max_length=16)
    job = StringField()
    cloth_spending = StringField()

    meta = {'collection': 'user'}

    def get_id(user_n):
        if user_n != "NULL":
            u_id = user.objects(username=user_n)[0]._id
        else:
            u_id = "NULL"
        return u_id

class userstyle(Document):
    _id = StringField()
    user_id = StringField()
    allmatch = IntField()
    artistic = IntField()
    baroque = IntField()
    bohemia = IntField()
    british = IntField()
    casual = IntField()
    elegant = IntField()
    folk = IntField()
    gentlewomanly = IntField()
    gothic = IntField()
    harajuku = IntField()
    hippie = IntField()
    hippop = IntField()
    japanese = IntField()
    korean = IntField()
    lolita = IntField()
    neutral = IntField()
    office = IntField()
    preppy = IntField()
    punk = IntField()
    sporty = IntField()
    street = IntField()
    sweet = IntField()
    vintage = IntField()
    western = IntField()
    workday = IntField()

    def style_info_update(style_set):
        # print(style_set)
        style_id = str(user.objects(username=style_set[0])[0]._id)
        # print(style_id)
        return update_sty(style_id, style_set)
