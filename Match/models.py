from mongoengine import *
import json
# from . main_match import main_match
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

    def get_id(user_n):
        if user_n != "NULL":
            u_id = user.objects(username=user_n)[0]._id
        else:
            u_id = "NULL"
        return u_id
