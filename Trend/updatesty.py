# id=user_id
# a=[user_id, style1, style2, ...]
import pymongo

def update_sty(id, a):

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    usersty = DB.userstyle
    # print(id)
    # print(usersty.find_one({'user_id': id}))
    if usersty.find_one({'user_id': id}):
        style = usersty.find_one({'user_id': id})
        for i in range(1, len(a)):
            style[a[i]] = style[a[i]]+1

        usersty.update({'user_id': id}, style)
        # print(usersty.find_one({'user_id': id}))
        return True
    else:
        return False


# print(update_sty('5ab4d352a15a171d586fe69e', ['', 'allmatch', 'casual']))