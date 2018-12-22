import math
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
DB = connection.WeWear
allcloth = DB.allcloth

tops = ['套头毛衣', '连帽卫衣', '衬衫', '圆领卫衣']
num2 = math.ceil(0.3 * len(tops))
array2 = []
action = [['女', '冬', '通勤'], ['女', '冬', '文艺'], ['女', '冬', '淑女'], ['女', '冬', '甜美'], ['女', '冬', '波西米亚'], ['女', '春', '通勤'], ['女', '春', '文艺'], ['女', '春', '淑女'], ['女', '春', '甜美'], ['女', '春', '波西米亚']]
if num2 != 0:
    for each in action:
        for i in range(0, num2):
            array = list(allcloth.find({"sex": each[0], "season": each[1], "style": each[2], "category2": tops[i]},
                                       {"id": 1, "_id": 0}))
            for j in array:
                array2.append(j['id'])
print(array2)
