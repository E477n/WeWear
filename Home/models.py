from django.db import models
from mongoengine import *
import json
from . search import search
from . updatesty import update_sty
connect('mydb', host='localhost', port=27017)

# Create your models here.

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

# users = user.objects.all()
# for i in users:
#     print("username:", i.username, ",password:", i.password, ",email:", i.email, ",sex:", i.sex, ",birthday:", i.birthday, ",spending:", i.cloth_spending)
# print("finish")

    def checkLogIn(user_n, user_p):
        user_exists = False
        login_permit = False
        u_info = {}
        user_filter = user.objects(username=user_n)
        if user_filter.count() == 1:
            user_exists = True
            user_info = user_filter[0]
            if user_p == user_info.password:
                login_permit = True
                u_email = user_info.email
                u_sex = user_info.sex
                u_birthday = user_info.birthday
                u_job = user_info.job
                u_info = {'username': user_n, 'email': u_email, 'sex': u_sex, 'birthday': str(u_birthday), 'job': u_job}
            else:
                login_permit = False
        else:
            user_exists = False
        login_condition = [{'user_exists': user_exists, 'login_permit': login_permit, 'user_info': u_info}]
        return json.dumps(login_condition)

    def checkSignIn(user_info):
        signin_user_exists = False
        user_filter = user.objects(username = user_info[1])
        if user_filter.count() == 1:
            signin_user_exists = True
        elif user_filter.count() == 0:
            signin_user_exists = False
            new_user = user(email=user_info[0], username=user_info[1], password=user_info[2], sex=user_info[3], birthday=user_info[4], job=user_info[5], cloth_spending=user_info[6])
            new_user.save(validate=False)
            search_id = str(user.objects(username=user_info[1])[0]._id)
            # print(search_id)
            search(search_id)
        return signin_user_exists

    def getUserInfoByUsername(um):
        user_obj = user.objects(username=um)[0]
        u_email = user_obj.email
        u_sex = user_obj.sex
        u_birthday = user_obj.birthday
        u_job = user_obj.job
        u_info = {'username': um, 'email': u_email, 'sex': u_sex, 'birthday': str(u_birthday), 'job': u_job}
        return json.dumps(u_info)


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