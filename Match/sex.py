import re


# 性别匹配
def sex_match(title):
    if re.search(r'男女', title):
        sex = '中'
    elif re.search(r'女', title):
        sex = '女'
    elif re.search(r'男', title):
        sex = '男'
    elif re.search(r'中性', title):
        sex = '中'
    else:
        sex = '中'
    return sex